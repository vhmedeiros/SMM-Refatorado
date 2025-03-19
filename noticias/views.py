from datetime import date, datetime
from django.core.cache import cache
from django.utils import timezone
from django.utils.timezone import make_aware, get_current_timezone, now
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.db.models import Q
from .models import NoticiaImportada
from .forms import NoticiaForm
from veiculos.models import Veiculosistemas, Municipio, Uf, TipoVeiculo

class NoticiaListView(ListView):
    model = NoticiaImportada
    template_name = "noticia_list.html"
    context_object_name = "noticias"
    paginate_by = 50

    def get_queryset(self):
        queryset = NoticiaImportada.objects.select_related("cd_veiculo").order_by("-dt_noticia")

        search = self.request.GET.get("search", "").strip()
        veiculo_nome = self.request.GET.get("veiculo", "").strip()
        estado = self.request.GET.get("uf", "").strip()
        data_inicio = self.request.GET.get("data_inicio", "")
        data_fim = self.request.GET.get("data_fim", "")

        if search:
            queryset = queryset.filter(Q(titulo__icontains=search) | Q(conteudo__icontains=search))

        if veiculo_nome:
            queryset = queryset.filter(cd_veiculo__nome_veiculo__icontains=veiculo_nome)

        if estado:  # 🔥 Correção para filtrar pela UF correta
            queryset = queryset.filter(cd_veiculo__cd_uf=estado)

        if data_inicio:
            try:
                data_inicio = timezone.make_aware(datetime.strptime(data_inicio, "%Y-%m-%d"))
                queryset = queryset.filter(dt_noticia__gte=data_inicio)
            except ValueError:
                pass

        if data_fim:
            try:
                data_fim = timezone.make_aware(datetime.strptime(data_fim, "%Y-%m-%d"))
                queryset = queryset.filter(dt_noticia__lte=data_fim)
            except ValueError:
                pass

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

    # def form_valid(self, form):
    #     noticia = form.save(commit=False)

    #     # Preenchendo a data de importação automaticamente

    #     # Verificar se o campo veículo foi preenchido corretamente
    #     cd_veiculo = self.request.POST.get("cd_veiculo")
    #     if cd_veiculo:
    #         noticia.cd_veiculo_id = cd_veiculo
    #     else:
    #         form.add_error(None, "Erro: Veículo não foi selecionado corretamente.")
    #         return self.form_invalid(form)

    #     noticia.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        form.instance.cd_veiculo_id = self.request.POST.get("cd_veiculo")  # Salva o ID do veículo certo
        return super().form_valid(form)

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

    # def form_valid(self, form):
    #     noticia = form.save(commit=False)
    #     if self.request.FILES.get("imagem"):
    #         noticia.imagem = self.request.FILES["imagem"]
    #     noticia.save()
    #     return super().form_valid(form)

    def form_valid(self, form):
        form.instance.cd_veiculo_id = self.request.POST.get("cd_veiculo")  # Atualiza corretamente
        return super().form_valid(form)

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

# def buscar_veiculos_popup(request):
#     query = request.GET.get("q", "").strip()
#     tipo_veiculo = request.GET.get("tipo_veiculo", "").strip()
#     estado = request.GET.get("estado", "").strip()

#     # 🔥 Buscar apenas veículos ativos (situacao_veiculo == 'A')
#     veiculos = Veiculosistemas.objects.filter(situacao_veiculo='A')

#     if query:
#         veiculos = veiculos.filter(nome_veiculo__icontains=query)
#     if tipo_veiculo:
#         veiculos = veiculos.filter(tipo_veiculo__tipo_veiculo=tipo_veiculo)
#     if estado:
#         veiculos = veiculos.filter(cd_uf__cd_uf=estado)

#     # 🔥 Limitar a 100 resultados para evitar lentidão
#     veiculos = veiculos[:100]

#     # Buscar tipos de veículos e estados únicos
#     tipos_veiculo = TipoVeiculo.objects.all()
#     estados = Uf.objects.all()

#     return render(request, "veiculos_popup.html", {
#         "veiculos": veiculos,
#         "tipos_veiculo": tipos_veiculo,
#         "estados": estados
#     })


def buscar_veiculos_popup(request):
    # 🚀 Obtém os veículos ativos do cache, se disponível
    veiculos = cache.get("veiculos_ativos")

    if not veiculos:
        veiculos = list(Veiculosistemas.objects.select_related("tipo_veiculo", "cd_uf")
                        .filter(situacao_veiculo="A")[:100])  # 🔥 Só veículos ativos
        cache.set("veiculos_ativos", veiculos, 300)  # 🔥 Cache por 5 minutos

    # 🚀 Obtém os tipos de veículo e estados do cache, se disponível
    tipos_veiculo = cache.get("tipos_veiculo")
    if not tipos_veiculo:
        tipos_veiculo = list(TipoVeiculo.objects.all())  # 🔥 Carregar apenas uma vez
        cache.set("tipos_veiculo", tipos_veiculo, 600)  # 🔥 Cache por 10 minutos

    estados = cache.get("estados")
    if not estados:
        estados = list(Uf.objects.all())  # 🔥 Carregar apenas uma vez
        cache.set("estados", estados, 600)  # 🔥 Cache por 10 minutos

    # 🔥 Obtém os filtros da requisição
    nome = request.GET.get("q", "")
    tipo = request.GET.get("tipo_veiculo", "")
    estado = request.GET.get("estado", "")

    # 🔥 Aplicar filtros se necessário
    veiculos_filtrados = veiculos
    if nome:
        veiculos_filtrados = [v for v in veiculos if nome.lower() in v.nome_veiculo.lower()]
    if tipo:
        veiculos_filtrados = [v for v in veiculos_filtrados if str(v.tipo_veiculo.tipo_veiculo) == tipo]
    if estado:
        veiculos_filtrados = [v for v in veiculos_filtrados if str(v.cd_uf.cd_uf) == estado]

    return render(request, "veiculos_popup.html", {
        "veiculos": veiculos_filtrados,
        "tipos_veiculo": tipos_veiculo,
        "estados": estados
    })


# def buscar_veiculos_popup(request):
#     """Exibe a listagem dos veículos ativos e permite filtrar por estado e tipo"""
#     nome = request.GET.get("q", "").strip()
#     tipo = request.GET.get("tipo_veiculo", "").strip()
#     estado = request.GET.get("estado", "").strip()

#     # 🔥 Filtrando veículos ativos
#     veiculos = Veiculosistemas.objects.filter(situacao_veiculo="A")

#     if nome:
#         veiculos = veiculos.filter(nome_veiculo__icontains=nome)
#     if tipo:
#         veiculos = veiculos.filter(tipo_veiculo_id=tipo)
#     if estado:
#         veiculos = veiculos.filter(cd_uf_id=estado)

#     # 🔥 Ordenar e limitar para evitar lentidão
#     veiculos = veiculos.order_by("nome_veiculo")[:100]

#     # Carregar os filtros corretamente
#     tipos_veiculo = TipoVeiculo.objects.all()
#     estados = Uf.objects.all()

#     return render(request, "veiculos_popup.html", {
#         "veiculos": veiculos,
#         "tipos_veiculo": tipos_veiculo,
#         "estados": estados,
#     })
