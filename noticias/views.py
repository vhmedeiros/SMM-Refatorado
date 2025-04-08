from datetime import date, datetime
from django.core.cache import cache
from django.core.paginator import Paginator
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
    paginate_by = 50 # colocar para 10

    def get_queryset(self):
        # queryset = NoticiaImportada.objects.select_related("cd_veiculo").order_by("-dt_noticia")
        

        search = self.request.GET.get("search", "").strip()
        veiculo_nome = self.request.GET.get("veiculo", "").strip()
        estado = self.request.GET.get("uf", "").strip()
        data_inicio = self.request.GET.get("data_inicio", "")
        data_fim = self.request.GET.get("data_fim", "")

        # 🔹 Definir queryset inicial
        if search or veiculo_nome or estado or data_inicio or data_fim:
            queryset = NoticiaImportada.objects.select_related("cd_veiculo").order_by("-dt_noticia")
        else:
            queryset = NoticiaImportada.objects.select_related("cd_veiculo").order_by("-dt_noticia")
            # 🔹 Se quiser que a lista inicie vazia, descomente a linha abaixo
            # queryset = NoticiaImportada.objects.none()

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
#     # 🚀 Obtém os veículos ativos do cache, se disponível
#     veiculos = cache.get("veiculos_ativos")

#     if not veiculos:
#         veiculos = list(Veiculosistemas.objects.select_related("tipo_veiculo", "cd_uf")
#                         .filter(situacao_veiculo="A")[:100])  # 🔥 Só veículos ativos
#         cache.set("veiculos_ativos", veiculos, 300)  # 🔥 Cache por 5 minutos

#     # 🚀 Obtém os tipos de veículo e estados do cache, se disponível
#     tipos_veiculo = cache.get("tipos_veiculo")
#     if not tipos_veiculo:
#         tipos_veiculo = list(TipoVeiculo.objects.all())  # 🔥 Carregar apenas uma vez
#         cache.set("tipos_veiculo", tipos_veiculo, 600)  # 🔥 Cache por 10 minutos

#     estados = cache.get("estados")
#     if not estados:
#         estados = list(Uf.objects.all())  # 🔥 Carregar apenas uma vez
#         cache.set("estados", estados, 600)  # 🔥 Cache por 10 minutos

#     # 🔥 Obtém os filtros da requisição
#     nome = request.GET.get("q", "")
#     tipo = request.GET.get("tipo_veiculo", "")
#     estado = request.GET.get("estado", "")

#     # 🔥 Aplicar filtros se necessário
#     veiculos_filtrados = veiculos
#     if nome:
#         veiculos_filtrados = [v for v in veiculos if nome.lower() in v.nome_veiculo.lower()]
#     if tipo:
#         veiculos_filtrados = [v for v in veiculos_filtrados if str(v.tipo_veiculo.tipo_veiculo) == tipo]
#     if estado:
#         veiculos_filtrados = [v for v in veiculos_filtrados if str(v.cd_uf.cd_uf) == estado]

#     return render(request, "veiculos_popup.html", {
#         "veiculos": veiculos_filtrados,
#         "tipos_veiculo": tipos_veiculo,
#         "estados": estados
#     })


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
