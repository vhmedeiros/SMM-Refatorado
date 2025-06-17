import csv
import requests
from collections import OrderedDict
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.timezone import localtime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponseForbidden, HttpResponse
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, FormView, View, TemplateView
from django.urls import reverse_lazy, reverse
from django.forms.models import inlineformset_factory
from django.template import engines
from clientes.models import ErpCliente
from noticias.models import NoticiaImportada
from veiculos.models import Veiculosistemas
from configuracoes.models import ConfiguracaoCliente
from palavras_chave.models import Categoriapalavrachave, Palavrachave
from .models import EmailDisparo, EmailHorarioDisparo, EmailDestinatario, EmailHistoricoDisparo, EmailDestinatarioBase
from .forms import EmailDisparoForm, EmailDestinatarioBaseForm, EmailDestinatarioBaseCSVForm, EmailDestinatarioForm, EmailHorarioDisparoForm
from .utils import gerar_conteudo_email, enviar_email_mailgrid, enviar_email_smtp

# === Inline formsets ===
EmailHorarioDisparoFormSet = inlineformset_factory(
    EmailDisparo,
    EmailHorarioDisparo,
    fields=["dia_semana", "horario"],
    extra=1,
    can_delete=True
)

EmailDestinatarioFormSet = inlineformset_factory(
    EmailDisparo,
    EmailDestinatario,
    fields=["nome", "email", "tipo", "ativo"],
    extra=1,
    can_delete=True
)

DIAS_SEMANA = OrderedDict([
    (0, 'Domingo'),
    (1, 'Segunda'),
    (2, 'Terça'),
    (3, 'Quarta'),
    (4, 'Quinta'),
    (5, 'Sexta'),
    (6, 'Sábado'),
])

# === Listagem dos disparos ===
class EmailDisparoListView(ListView):
    model = EmailDisparo
    template_name = "emails/email_list.html"
    context_object_name = "disparos"

    def get_queryset(self):
        return EmailDisparo.objects.filter(id_cliente=self.kwargs['id_cliente']).order_by('assunto')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_cliente"] = self.kwargs["id_cliente"]
        return context

class EmailDisparoCreateView(CreateView):
    model = EmailDisparo
    template_name = "emails/email_create.html"
    form_class = EmailDisparoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_cliente"] = self.kwargs["id_cliente"]
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        kwargs["cliente"] = cliente
        return kwargs

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.id_cliente_id = self.kwargs["id_cliente"]
            self.object.save()
            form.save_m2m()
            messages.success(self.request, "✅ Disparo criado com sucesso!")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"❌ Erro ao criar o disparo: {str(e)}")
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"❌ Erro ao criar o disparo: {form.errors.as_text()}")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("emails:email_detail", kwargs={
            "id_cliente": self.kwargs["id_cliente"],
            "pk": self.object.pk
        })

class EmailDisparoUpdateView(UpdateView):
    model = EmailDisparo
    template_name = "emails/email_update.html"
    form_class = EmailDisparoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_cliente"] = self.kwargs["id_cliente"]
        context["id_disparo"] = self.object.pk
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        kwargs["cliente"] = cliente
        return kwargs

    def form_valid(self, form):
        try:
            self.object = form.save(commit=False)
            self.object.id_cliente_id = self.kwargs["id_cliente"]
            self.object.save()
            form.save_m2m()
            messages.success(self.request, "✅ Disparo atualizado com sucesso!")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"❌ Erro ao atualizar o disparo: {str(e)}")
            return super().form_invalid(form)

    def form_invalid(self, form):
        messages.error(self.request, f"❌ Erro ao atualizar o disparo: {form.errors.as_text()}")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy("emails:email_update", kwargs={
            "id_cliente": self.kwargs["id_cliente"],
            "pk": self.object.pk
        })


class EmailDisparoDetailView(DetailView):
    model = EmailDisparo
    template_name = "emails/email_detail.html"
    context_object_name = "disparo"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["id_cliente"] = self.kwargs["id_cliente"]
        context["historico"] = EmailHistoricoDisparo.objects.filter(id_email_disparo=self.object.pk)
        context["horarios"] = EmailHorarioDisparo.objects.filter(id_email_disparo=self.object.pk).order_by("dia_semana", "horario")
        context["destinatarios"] = EmailDestinatario.objects.filter(id_email_disparo=self.object.pk).order_by("email")
        return context

# === Alterna status ATIVO/INATIVO de um disparo ===
class EmailDisparoToggleStatusView(View):
    def post(self, request, id_cliente, pk):
        disparo = get_object_or_404(EmailDisparo, pk=pk, id_cliente=id_cliente)
        disparo.status = "INATIVO" if disparo.status == "ATIVO" else "ATIVO"
        disparo.save()
        return HttpResponseRedirect(reverse('emails:email_list', kwargs={'id_cliente': id_cliente}))

# === Listagem de destinatários base ===
class EmailDestinatarioBaseListView(ListView):
    model = EmailDestinatarioBase
    template_name = "destinatarios_base/destinatario_base_list.html"
    context_object_name = "destinatarios"

    def get_queryset(self):
        return EmailDestinatarioBase.objects.filter(id_cliente=self.kwargs['id_cliente']).order_by('grupo','nome', 'tipo',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_cliente'] = self.kwargs['id_cliente']
        context['cliente'] = get_object_or_404(ErpCliente, pk=self.kwargs['id_cliente'])
        return context

# === Criação de destinatário base ===
class EmailDestinatarioBaseCreateView(CreateView):
    model = EmailDestinatarioBase
    template_name = "destinatarios_base/destinatario_base_create.html"
    form_class = EmailDestinatarioBaseForm

    def form_valid(self, form):
        form.instance.id_cliente_id = self.kwargs['id_cliente']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_cliente'] = self.kwargs['id_cliente']
        context['cliente'] = get_object_or_404(ErpCliente, pk=self.kwargs['id_cliente'])
        return context

    def get_success_url(self):
        return reverse_lazy('emails:destinatario_base_list', kwargs={'id_cliente': self.kwargs['id_cliente']})

# === Edição de destinatário base ===
class EmailDestinatarioBaseUpdateView(UpdateView):
    model = EmailDestinatarioBase
    template_name = "destinatarios_base/destinatario_base_update.html"
    form_class = EmailDestinatarioBaseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['destinatario'] = self.object # permite que o template acesse o destinatário atual
        context['id_cliente'] = self.object.id_cliente_id
        return context

    def get_success_url(self):
        return reverse_lazy('emails:destinatario_base_list', kwargs={'id_cliente': self.object.id_cliente_id})

# === Exclusão de destinatário base ===
class EmailDestinatarioBaseDeleteView(DeleteView):
    model = EmailDestinatarioBase
    template_name = "destinatarios_base/destinatario_base_delete.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_cliente'] = self.object.id_cliente_id
        return context

    def get_success_url(self):
        return reverse_lazy('emails:destinatario_base_list', kwargs={'id_cliente': self.object.id_cliente_id})

# importar CSV
class EmailDestinatarioBaseCSVImportView(FormView):
    template_name = "destinatarios_base/destinatario_base_csv_import.html"
    form_class = EmailDestinatarioBaseCSVForm

    def form_valid(self, form):
        id_cliente = self.kwargs['id_cliente']
        csv_file = form.cleaned_data['csv_file']
        
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)

        sucesso, erros = 0, 0

        for row in reader:
            # remover espaços em branco e converter para minúsculas
            row = {k.strip(): v.strip() for k, v in row.items()}

            # validação minima
            if not row.get('email') or not row.get('tipo'):
                erros += 1
                messages.error(self.request, f"Linha incompleta: email e tipo são obrigatórios. Dados: {row}")
                continue

            try:
                EmailDestinatarioBase.objects.create(
                    id_cliente_id=id_cliente,
                    nome=row.get('nome') or None,
                    email=row['email'],
                    grupo=row.get('grupo') or None,
                    tipo=row.get('tipo'),
                    ativo=str(row.get('ativo', '1')).lower() in ['1', 'true', 'sim', 's'],
                )
                sucesso += 1

            except Exception as e:
                    erros += 1
                    messages.error(self.request, f"Erro ao importar '{row.get('email')}': {str(e)}")
        
        messages.success(self.request, f"{sucesso} destinatários importados com sucesso!")
        
        if erros:
            messages.warning(self.request, f"{erros} erros ocorreram durante a importação.")
        return redirect("emails:destinatario_base_list", id_cliente=id_cliente)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id_cliente'] = self.kwargs['id_cliente']
        return context

# modelo de CSV
def baixar_modelo_destinatarios_csv(request, id_cliente):
    # Gera um arquivo CSV de exemplo para importação de destinatários base.
    from django.http import HttpResponse
    import csv

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="modelo_destinatarios.csv"'

    writer = csv.writer(response)
    writer.writerow(['nome', 'email', 'grupo', 'tipo', 'ativo'])
    writer.writerow(['João Silva', 'joao@email.com', 'Administrativo', 'PRINCIPAL', '1'])
    writer.writerow(['Maria Souza', 'maria@email.com', 'Jurídico', 'CCO', '1'])
    writer.writerow(['', 'teste@email.com', '', 'CC', '0'])  # exemplo com campos opcionais vazios

    return response

# Views para Create/Update de horários
class EmailHorarioDisparoManageView(TemplateView):
    template_name = "horarios/horarios_manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_cliente = kwargs['id_cliente']
        id_disparo = kwargs['id_disparo']
        disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
        destinatarios = EmailDestinatario.objects.filter(id_email_disparo=disparo)

        context.update({
            'id_cliente': id_cliente,
            'disparo': disparo,
            'destinatarios': destinatarios,
        })
        return context



# === VIEWS HTMX ===
# ⏰ HTMX – Listar horários
def htmx_list_horarios(request, id_cliente, id_disparo):
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    horarios = EmailHorarioDisparo.objects.filter(id_email_disparo=disparo)
    
    return render(request, "partials/_horario_list.html", {
        "disparo": disparo,
        "horarios": horarios,
        "id_cliente": id_cliente,
        "dias_da_semana": DIAS_SEMANA,  # <-- isso que faltava
    })

# ⏰ HTMX – Adicionar horário
def htmx_add_horario(request, id_cliente, id_disparo):
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    dia_forcado = request.GET.get("dia")
    form = EmailHorarioDisparoForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.instance.id_email_disparo = disparo
        form.save()
        horarios = EmailHorarioDisparo.objects.filter(id_email_disparo=disparo)
        return render(request, "partials/_dia_horario.html", {
            "codigo_dia": int(form.instance.dia_semana),
            "nome_dia": DIAS_SEMANA[int(form.instance.dia_semana)],
            "horarios": horarios,
            "disparo": disparo,
            "id_cliente": id_cliente,
            "form": EmailHorarioDisparoForm(initial={"dia_semana": form.instance.dia_semana}),
        })

    # Se for GET (abrir formulário), força o dia selecionado no campo hidden
    if dia_forcado:
        form.initial["dia_semana"] = dia_forcado

    return render(request, "partials/_form_horario.html", {
        "form": form,
        "disparo": disparo,
        "id_cliente": id_cliente,
        "codigo_dia": int(dia_forcado) if dia_forcado else None
    })

def htmx_edit_horario(request, id_cliente, pk):
    horario = get_object_or_404(EmailHorarioDisparo, pk=pk)
    disparo = horario.id_email_disparo
    if disparo.id_cliente_id != id_cliente:
        return HttpResponse(status=403)

    form = EmailHorarioDisparoForm(request.POST or None, instance=horario)
    if request.method == "POST" and form.is_valid():
        form.save()
        # Após salvar, renderiza só o dia do horário editado
        codigo_dia = form.instance.dia_semana
        horarios = EmailHorarioDisparo.objects.filter(id_email_disparo=disparo)
        return render(request, "partials/_dia_horario.html", {
            "codigo_dia": codigo_dia,
            "nome_dia": DIAS_SEMANA[codigo_dia],
            "horarios": horarios,
            "disparo": disparo,
            "id_cliente": id_cliente,
        })

    return render(request, "partials/_form_horario.html", {
        "form": form,
        "disparo": disparo,
        "horario": horario,
        "id_cliente": id_cliente,
    })

# ⏰ HTMX – Remover horário
def htmx_delete_horario(request, id_cliente, pk):
    horario = get_object_or_404(EmailHorarioDisparo, pk=pk)
    disparo = horario.id_email_disparo
    if disparo.id_cliente_id != id_cliente:
        return HttpResponse(status=403)

    codigo_dia = horario.dia_semana
    horario.delete()

    horarios = EmailHorarioDisparo.objects.filter(id_email_disparo=disparo)
    return render(request, "partials/_dia_horario.html", {
        "codigo_dia": codigo_dia,
        "nome_dia": DIAS_SEMANA[codigo_dia],
        "horarios": horarios,
        "disparo": disparo,
        "id_cliente": id_cliente,
    })


# View para Create/Update Destinatários
class EmailDestinatarioManageView(TemplateView):
    template_name = "destinatarios/destinatarios_manage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_cliente = kwargs["id_cliente"]
        id_disparo = kwargs["id_disparo"]
        disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)

        # Pega os grupos únicos disponíveis na base
        grupos = EmailDestinatarioBase.objects.filter(id_cliente_id=id_cliente).values_list("grupo", flat=True).distinct()

        context.update({
            "id_cliente": id_cliente,
            "disparo": disparo,
            "grupos": grupos,
        })
        return context

# 👥 HTMX – destinatários
def htmx_list_destinatarios(request, id_cliente, id_disparo):
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    destinatarios = EmailDestinatario.objects.filter(id_email_disparo=disparo)
    return render(request, "partials/_destinatario_list.html", {
        "disparo": disparo,
        "destinatarios": destinatarios,
        "id_cliente": id_cliente,
    })

def htmx_add_destinatario(request, id_cliente, id_disparo):
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    form = EmailDestinatarioForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.instance.id_email_disparo = disparo
        form.save()
        return htmx_list_destinatarios(request, id_cliente, id_disparo)
    return render(request, "partials/_form_destinatario.html", {
        "form": form,
        "disparo": disparo,
        "id_cliente": id_cliente,
        "destinatario": form.instance,  # Passa o destinatário vazio para o template
    })

# HTMX – Editar destinatário
def htmx_edit_destinatario(request, id_cliente, pk):
    destinatario = get_object_or_404(EmailDestinatario, pk=pk)
    disparo = destinatario.id_email_disparo

    if disparo.id_cliente_id != id_cliente:
        return HttpResponse(status=403)

    form = EmailDestinatarioForm(request.POST or None, instance=destinatario)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            # Atualiza a lista completa de destinatários após salvar
            return htmx_list_destinatarios(request, id_cliente, disparo.pk)
        else:
            # Debug opcional (pode remover depois)
            print("Erros no formulário:", form.errors)

    return render(request, "partials/_form_destinatario.html", {
        "form": form,
        "destinatario": destinatario,
        "disparo": disparo,
        "id_cliente": id_cliente,
    })


def htmx_delete_destinatario(request, id_cliente, pk):
    destinatario = get_object_or_404(EmailDestinatario, pk=pk)
    disparo = destinatario.id_email_disparo
    if disparo.id_cliente_id != id_cliente:
        return HttpResponse(status=403)

    destinatario.delete()
    return htmx_list_destinatarios(request, id_cliente, disparo.pk)

def htmx_grupo_destinatarios(request, id_cliente, id_disparo):
    grupos = EmailDestinatarioBase.objects.filter(id_cliente_id=id_cliente).values_list("grupo", flat=True).distinct()
    return render(request, "partials/_grupo_destinatario_select.html", {
        "grupos": grupos,
        "id_cliente": id_cliente,
        "id_disparo": id_disparo,
    })

def htmx_importar_grupo_destinatarios(request, id_cliente, id_disparo):
    grupo = request.GET.get("grupo")
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)

    # Evitar duplicidade
    emails_existentes = EmailDestinatario.objects.filter(id_email_disparo=disparo).values_list("email", flat=True)

    base_destinatarios = EmailDestinatarioBase.objects.filter(id_cliente=disparo.id_cliente, grupo=grupo)

    for base in base_destinatarios:
        if base.email not in emails_existentes:
            EmailDestinatario.objects.create(
                id_email_disparo=disparo,
                nome=base.nome,
                email=base.email,
                tipo=base.tipo,
                ativo=True
            )

    return htmx_list_destinatarios(request, id_cliente, id_disparo)



# ✅ HTMX – Alternar status de destinatário (ativar/inativar)
@csrf_exempt
def htmx_toggle_destinatario(request, id_cliente, pk):
    destinatario = get_object_or_404(EmailDestinatario, pk=pk)
    disparo = destinatario.id_email_disparo

    if disparo.id_cliente_id != id_cliente:
        return HttpResponseForbidden()

    ativo = request.POST.get("ativo")
    if ativo is not None:
        destinatario.ativo = ativo.lower() == "true"
        destinatario.save()

    return render(request, "partials/_destinatario_item.html", {
        "destinatario": destinatario,
        "disparo": disparo,
        "id_cliente": id_cliente
    })


def preview_email_render(request, id_cliente, id_disparo):
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    data_str = request.GET.get("data")

    if not data_str:
        return HttpResponseBadRequest("Parâmetro de data inválido")

    def parse_data(input_str):
        try:
            if "|" in input_str:
                partes = input_str.split("|")
                dt_inicio = datetime.strptime(partes[0].strip(), "%d/%m/%Y")
                dt_fim = datetime.strptime(partes[1].strip(), "%d/%m/%Y")
            else:
                dt_inicio = datetime.strptime(input_str.strip(), "%d/%m/%Y")
                dt_fim = dt_inicio
            return dt_inicio, dt_fim
        except Exception:
            return None, None

    dt_inicio, dt_fim = parse_data(data_str)
    if not dt_inicio or not dt_fim:
        return HttpResponseBadRequest("Formato de data inválido.")

    palavras = Palavrachave.objects.filter(id_categoria__in=disparo.categorias.all())

    query = Q()
    for palavra in palavras:
        query |= Q(titulo__icontains=palavra.palavra) | Q(conteudo__icontains=palavra.palavra)

    noticias = NoticiaImportada.objects.filter(
        dt_noticia__range=(dt_inicio, dt_fim)
    ).filter(query).select_related('cd_veiculo')

    # Agrupar por veículo
    agrupadas = {}
    for noticia in noticias:
        nome_veiculo = noticia.cd_veiculo.nome_veiculo.upper() if noticia.cd_veiculo else "SEM VEÍCULO"
        agrupadas.setdefault(nome_veiculo, []).append(noticia)

    # Links de cada notícia
    configuracao_cliente = get_object_or_404(ConfiguracaoCliente, id_cliente=disparo.id_cliente)

    links_noticias = {}
    for noticia in noticias:
        url = reverse("noticia_detail", kwargs={
            "sigla_cliente": configuracao_cliente.sigla_cliente,
            "cd_noticia": noticia.cd_noticia
        })
        links_noticias[noticia.cd_noticia] = request.build_absolute_uri(url)

    logo_url = configuracao_cliente.logotipo.url if configuracao_cliente.logotipo else ""
    data_envio = datetime.now().strftime("%A, %d de %B de %Y").capitalize()
    nome_cliente = configuracao_cliente.nome_cliente_sistema

    return render(request, "emails/components/email_base_render.html", {
        "estilo_geral": disparo.estilo_geral,
        "cabecalho_html": disparo.cabecalho_html,
        "titulo_html": disparo.titulo_html,
        "rodape_html": disparo.rodape_html,
        "agrupadas": agrupadas,
        "logo_url": logo_url,
        "data_envio": data_envio,
        "nome_cliente": nome_cliente,
        "links_noticias": links_noticias,
    })


@csrf_exempt  # Permite POST sem verificação de CSRF (se for necessário para integração externa)
def enviar_email_simples(request, id_cliente, id_disparo):
    # Busca o disparo do cliente com base nos IDs informados
    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)

    # Garante que seja um POST
    if request.method != "POST":
        return HttpResponseBadRequest("Requisição inválida.")

    # Coleta os dados do formulário
    destinatario = request.POST.get("email_destinatario")
    data_str = request.POST.get("data_edicao")

    # Verifica se os campos obrigatórios foram preenchidos
    if not destinatario or not data_str:
        messages.error(request, "E-mail e data são obrigatórios.")
        return redirect(reverse("emails:email_detail", args=[id_cliente, id_disparo]))

    # Função interna para interpretar a string de data fornecida pelo usuário
    def parse_data(input_str):
        try:
            if "|" in input_str:
                partes = input_str.split("|")
                dt_inicio = datetime.strptime(partes[0].strip(), "%d/%m/%Y")
                if len(partes[1].strip()) <= 5:
                    hora = datetime.strptime(partes[1].strip(), "%H:%M").time()
                    dt_fim = datetime.combine(dt_inicio, hora)
                else:
                    dt_fim = datetime.strptime(partes[1].strip(), "%d/%m/%Y %H:%M")
            elif len(input_str.strip()) <= 10:
                dt_inicio = datetime.strptime(input_str.strip(), "%d/%m/%Y")
                dt_fim = dt_inicio
            else:
                dt_inicio = datetime.strptime(input_str.strip(), "%d/%m/%Y %H:%M")
                dt_fim = dt_inicio
            return dt_inicio, dt_fim
        except Exception:
            return None, None

    # Aplica o parser à string de data
    dt_inicio, dt_fim = parse_data(data_str)
    if not dt_inicio or not dt_fim:
        messages.error(request, "Formato de data inválido.")
        return redirect(reverse("emails:email_detail", args=[id_cliente, id_disparo]))

    # Filtra as notícias com base no intervalo de data e nos veículos associados à categoria
    veiculos = Veiculosistemas.objects.filter(
        categoriapalavrachave_in=disparo.categorias.all()
    ).distinct()

    noticias = NoticiaImportada.objects.filter(
        dt_noticia__range=(dt_inicio, dt_fim),
        cd_veiculo__in=veiculos
    )


    # Garante que exista pelo menos uma notícia para enviar
    if not noticias.exists():
        messages.warning(request, "Nenhuma notícia encontrada para este período.")
        return redirect(reverse("emails:email_detail", args=[id_cliente, id_disparo]))

    # Renderiza o HTML do e-mail com base no template e dados do disparo
    html_email = render_to_string("emails/components/email_base_render.html", {
        "estilo_geral": disparo.estilo_geral,
        "cabecalho_html": disparo.cabecalho_html,
        "titulo_html": disparo.titulo_html,
        "rodape_html": disparo.rodape_html,
        "noticias": noticias,
    })

    # Monta o payload para a API da Mailgrid
    payload = {
        "from": "contato@smmclipping.com.br",
        "to": [destinatario],
        "subject": disparo.assunto,
        "html": html_email
    }

    # Envia o e-mail e registra o resultado
    try:
        response = requests.post(
            "https://api.mailgrid.com.br/send-email",
            headers={"Authorization": "Bearer SUA_API_KEY"},  # Substitua pela sua chave real
            json=payload
        )

        if response.status_code == 200:
            status = "ENVIADO"
            msg = "E-mail enviado com sucesso."
            messages.success(request, msg)
        else:
            status = "FALHA"
            msg = f"Erro {response.status_code}: {response.text}"
            messages.error(request, msg)

    except Exception as e:
        status = "ERRO"
        msg = str(e)
        messages.error(request, "Falha ao enviar o e-mail.")

    # Salva o histórico do disparo, independentemente do sucesso ou erro
    EmailHistoricoDisparo.objects.create(
        id_email_disparo=disparo,
        data_hora_agendada=datetime.now(),
        data_hora_enviada=datetime.now(),
        status=status,
        mensagem_retorno=msg
    )

    # Redireciona de volta para os detalhes do disparo
    return redirect(reverse("emails:email_detail", args=[id_cliente, id_disparo]))

@csrf_exempt
def enviar_email_manual(request, id_cliente, id_disparo):
    if request.method != "POST":
        return JsonResponse({"erro": "Método não permitido"}, status=405)

    disparo = get_object_or_404(EmailDisparo, pk=id_disparo, id_cliente_id=id_cliente)
    email_destino = request.POST.get("email")
    data_str = request.POST.get("data")

    if not email_destino or not data_str:
        return JsonResponse({"erro": "Campos obrigatórios não enviados"}, status=400)

    def parse_data(input_str):
        try:
            if '|' in input_str:
                partes = input_str.split('|')
                dt_inicio = datetime.strptime(partes[0].strip(), "%d/%m/%Y")
                dt_fim = datetime.strptime(partes[1].strip(), "%d/%m/%Y")
            elif len(input_str.strip()) <= 10:
                dt_inicio = datetime.strptime(input_str.strip(), "%d/%m/%Y")
                dt_fim = dt_inicio
            else:
                dt_inicio = datetime.strptime(input_str.strip(), "%d/%m/%Y %H:%M")
                dt_fim = dt_inicio
            return dt_inicio, dt_fim
        except Exception:
            return None, None

    dt_inicio, dt_fim = parse_data(data_str)
    if not dt_inicio or not dt_fim:
        return JsonResponse({"erro": "Formato de data inválido"}, status=400)

    palavras = Palavrachave.objects.filter(id_categoria__in=disparo.categorias.all())

    query = Q()
    for palavra in palavras:
        query |= Q(titulo__icontains=palavra.palavra) | Q(conteudo__icontains=palavra.palavra)

    noticias = NoticiaImportada.objects.filter(
        dt_noticia__date__range=(dt_inicio.date(), dt_fim.date())
    ).filter(query).select_related('cd_veiculo')

    # Agrupar por veículo
    agrupadas = {}
    for noticia in noticias:
        veiculo_nome = noticia.cd_veiculo.nome_veiculo.upper() if noticia.cd_veiculo else "SEM VEÍCULO"
        if veiculo_nome not in agrupadas:
            agrupadas[veiculo_nome] = []
        agrupadas[veiculo_nome].append(noticia)

    # Obter configuração do cliente
    configuracao_cliente = get_object_or_404(ConfiguracaoCliente, id_cliente=disparo.id_cliente)

    # Gerar links para cada notícia
    links_noticias = {}
    for noticia in noticias:
        url = reverse("noticia_detail", kwargs={
            "sigla_cliente": configuracao_cliente.sigla_cliente,
            "cd_noticia": noticia.cd_noticia
        })
        full_url = request.build_absolute_uri(url)
        links_noticias[noticia.cd_noticia] = full_url

    logo_url = configuracao_cliente.logotipo.url if configuracao_cliente.logotipo and hasattr(configuracao_cliente.logotipo, 'url') else ""
    data_envio = datetime.now().strftime("%d/%m/%Y")
    nome_cliente = configuracao_cliente.nome_cliente_sistema

    corpo_html = render_to_string("emails/components/email_base_render.html", {
        "estilo_geral": disparo.estilo_geral,
        "cabecalho_html": disparo.cabecalho_html,
        "titulo_html": disparo.titulo_html,
        "rodape_html": disparo.rodape_html,
        "agrupadas": agrupadas,
        "logo_url": logo_url,
        "data_envio": data_envio,
        "nome_cliente": nome_cliente,
        "links_noticias": links_noticias,
    })

    resposta = enviar_email_smtp(
        destinatarios=[email_destino],
        assunto=disparo.assunto,
        corpo_html=corpo_html
    )

    if resposta["status"] == "ok":
        return JsonResponse({"mensagem": "E-mail enviado com sucesso via SMTP!"})
    else:
        return JsonResponse({"erro": "Falha ao enviar", "detalhes": resposta.get("mensagem")}, status=500)