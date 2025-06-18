from datetime import date, datetime
from django.core.cache import cache
from django.core.paginator import Paginator
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone, now
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import FormView
from django.db.models import Q
from .models import NoticiaImportada, NoticiaImagem
from .forms import NoticiaForm, NoticiaImagemForm
from veiculos.models import Veiculosistemas, Municipio, Uf, TipoVeiculo

class NoticiaListView(ListView):
    model = NoticiaImportada
    template_name = "noticia_list.html"
    context_object_name = "noticias"
    paginate_by = 50 # colocar para 10

    def get_queryset(self):
        queryset = NoticiaImportada.objects.select_related("cd_veiculo").order_by("-dt_noticia")

        # Pegando parâmetros GET
        params = self.request.GET
        search = params.get("search", "").strip()
        veiculo_nome = params.get("veiculo", "").strip()
        estado = params.get("uf", "").strip()
        data_inicio = params.get("data_inicio", "").strip()
        data_fim = params.get("data_fim", "").strip()

        # 🔍 Se não houver nenhum parâmetro GET (ou seja, o usuário ainda não clicou em "Filtrar"), não retorna nada
        if not params:
            return queryset.none()

        # 🔍 Se o usuário clicou em "Filtrar" mas não preencheu as datas, usar o intervalo de hoje
        if not data_inicio and not data_fim:
            hoje = timezone.now().date()
            inicio_dia = timezone.make_aware(datetime.combine(hoje, datetime.min.time()))
            fim_dia = timezone.make_aware(datetime.combine(hoje, datetime.max.time()))
            queryset = queryset.filter(dt_noticia__range=(inicio_dia, fim_dia))
        else:
            # Se o usuário preencheu as datas, usar os valores fornecidos
            if data_inicio:
                try:
                    data_inicio = timezone.make_aware(datetime.strptime(data_inicio, "%Y-%m-%dT%H:%M"))
                    queryset = queryset.filter(dt_noticia__gte=data_inicio)
                except ValueError:
                    pass

            if data_fim:
                try:
                    data_fim = timezone.make_aware(datetime.strptime(data_fim, "%Y-%m-%dT%H:%M"))
                    queryset = queryset.filter(dt_noticia__lte=data_fim)
                except ValueError:
                    pass

        # Aplicar demais filtros (se houver)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search) | Q(conteudo__icontains=search))

        if veiculo_nome:
            queryset = queryset.filter(cd_veiculo__nome_veiculo__icontains=veiculo_nome)

        if estado:
            queryset = queryset.filter(cd_veiculo__cd_uf=estado)

        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estados"] = Uf.objects.order_by("nome_uf")  # UFs cadastradas no banco
        context["veiculos"] = Veiculosistemas.objects.all()  # Veículos disponíveis
        context["data_inicio"] = self.request.GET.get("data_inicio", str(date.today()))
        context["data_fim"] = self.request.GET.get("data_fim", str(date.today()))
        return context
        
class NoticiaCreateView(CreateView):
    model = NoticiaImportada
    form_class = NoticiaForm
    template_name = "noticia_create.html"
    success_url = reverse_lazy("noticia_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["imagem_form"] = NoticiaImagemForm(self.request.POST or None, self.request.FILES or None)
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        imagem_form = NoticiaImagemForm(self.request.POST, self.request.FILES)
        if imagem_form.is_valid() and imagem_form.cleaned_data.get("caminho_imagem"):
            nova_imagem = imagem_form.save(commit=False)
            nova_imagem.noticia = self.object
            nova_imagem.save()

        return response

class NoticiaDetailView(DetailView):
    model = NoticiaImportada
    template_name = "partials/noticia_detail_partial.html"
    context_object_name = "noticia"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            return render(self.request, "partials/noticia_detail_partial.html", context)
        return super().render_to_response(context, **response_kwargs)

class NoticiaUpdateView(UpdateView):
    model = NoticiaImportada
    template_name = "noticia_update.html"
    form_class = NoticiaForm
    success_url = reverse_lazy("noticia_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_id = self.object.cd_noticia

        # Próxima e Anterior
        context["proxima_noticia"] = NoticiaImportada.objects.filter(cd_noticia__gt=current_id).order_by('cd_noticia').first()
        context["anterior_noticia"] = NoticiaImportada.objects.filter(cd_noticia__lt=current_id).order_by('-cd_noticia').first()

        # Form de imagem
        context["imagem_form"] = NoticiaImagemForm()

        # Imagens já existentes
        context["imagens_vinculadas"] = self.object.imagens.all()

        return context

# para inserir imagens
class NoticiaImagemCreateView(FormView):
    form_class = NoticiaImagemForm
    template_name = 'noticia_imagem_form.html'  # Caso queira criar um template separado (opcional)

    def form_valid(self, form):
        noticia = get_object_or_404(NoticiaImportada, pk=self.kwargs['pk'])
        imagem = form.save(commit=False)
        imagem.noticia = noticia
        imagem.save()
        return redirect('noticia_update', pk=noticia.pk)

def buscar_cidades(request):
    uf = request.GET.get("uf")
    if uf:
        cidades = Veiculosistemas.objects.filter(cd_uf=uf).values("id_municipio", "nome_veiculo")
        return JsonResponse(list(cidades), safe=False)
    return JsonResponse([], safe=False)


def buscar_veiculos(request):
    query = request.GET.get("q", "").strip()

    print(f"DEBUG: Query recebida -> {query}")  # Verificar se o termo de busca está correto

    if not query:
        return HttpResponse("")

    veiculos = Veiculosistemas.objects.filter(
        nome_veiculo__icontains=query
    ).values("cd_veiculo", "nome_veiculo")[:10]

    print(f"DEBUG: Veículos encontrados -> {list(veiculos)}")  # Verificar se encontrou veículos

    if not veiculos:
        return HttpResponse("<div class='dropdown-menu show'><li class='list-group-item disabled'>Nenhum veículo encontrado</li></div>")

    # Gerando a lista de sugestões
    html = "<div class='dropdown-menu show'>"
    for v in veiculos:
        html += f"""
            <button class="dropdown-item"
                    onclick="document.getElementById('veiculo-autocomplete').value = '{v['nome_veiculo']}';
                             document.getElementById('sugestoes-veiculo').classList.remove('show');">
                {v["nome_veiculo"]}
            </button>
        """
    html += "</div>"

    return HttpResponse(html)


def buscar_veiculos_popup(request):
    # 🔍 Filtros recebidos
    nome = request.GET.get("q", "")
    tipo = request.GET.get("tipo_veiculo", "")
    estado = request.GET.get("estado", "")

    # 🔍 Query base otimizada: filtra no banco (não carrega tudo em memória!)
    veiculos = Veiculosistemas.objects.select_related("tipo_veiculo", "cd_uf").filter(situacao_veiculo="A")

    if nome:
        veiculos = veiculos.filter(nome_veiculo__icontains=nome)
    if tipo:
        veiculos = veiculos.filter(tipo_veiculo__tipo_veiculo=tipo)
    if estado:
        veiculos = veiculos.filter(cd_uf__cd_uf=estado)

    # 🔁 Paginação para não sobrecarregar o HTML/servidor
    paginator = Paginator(veiculos, 30)  # 30 veículos por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # 🔥 Cache leve para tipos e estados
    tipos_veiculo = cache.get("tipos_veiculo")
    if not tipos_veiculo:
        tipos_veiculo = list(TipoVeiculo.objects.all())
        cache.set("tipos_veiculo", tipos_veiculo, 600)

    estados = cache.get("estados")
    if not estados:
        estados = list(Uf.objects.all())
        cache.set("estados", estados, 600)

    return render(request, "veiculos_popup.html", {
        "page_obj": page_obj,
        "veiculos": page_obj.object_list,
        "tipos_veiculo": tipos_veiculo,
        "estados": estados,
        "paginator": paginator,
    })
