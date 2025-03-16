from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import Q
from .models import NoticiaImportada
from .forms import NoticiaForm
from veiculos.models import Veiculosistemas, Municipio, Uf

# class NoticiaListView(ListView):
#     model = NoticiaImportada
#     template_name = "noticia_list.html"
#     context_object_name = "noticias"

#     def get_queryset(self):
#         queryset = NoticiaImportada.objects.select_related("cd_veiculo").only(
#             "cd_noticia", "dt_noticia", "titulo", "cd_veiculo__nome_veiculo"
#         ).order_by("-dt_noticia")

#         titulo = self.request.GET.get("titulo", "").strip()
#         veiculo = self.request.GET.get("veiculo", "").strip()
#         uf = self.request.GET.get("uf", "").strip()
#         cidade = self.request.GET.get("cidade", "").strip()

#         if titulo or veiculo or uf or cidade:  # 🔹 Evita carregar tudo sem necessidade
#             if titulo:
#                 queryset = queryset.filter(Q(titulo__icontains=titulo))
#             if veiculo:
#                 queryset = queryset.filter(cd_veiculo__nome_veiculo__icontains=veiculo)
#             if uf:
#                 queryset = queryset.filter(cd_veiculo__cd_uf=uf)
#             if cidade:
#                 queryset = queryset.filter(cd_veiculo__id_municipio=cidade)
#         else:
#             queryset = NoticiaImportada.objects.none()  # 🔹 Retorna lista vazia ao carregar a página

#         return queryset

#     def render_to_response(self, context, **response_kwargs):
#         if self.request.headers.get("HX-Request"):  # 🔹 Responde apenas via HTMX
#             return render(self.request, "partials/noticia_list_partial.html", context)
#         return super().render_to_response(context, **response_kwargs)

class NoticiaListView(ListView):
    model = NoticiaImportada
    template_name = "noticia_list.html"
    context_object_name = "noticias"

    def get_queryset(self):
        queryset = NoticiaImportada.objects.select_related("cd_veiculo").only(
            "cd_noticia", "dt_noticia", "titulo", "cd_veiculo__nome_veiculo", "cd_veiculo__cd_uf", "cd_veiculo__id_municipio"
        ).order_by("-dt_noticia")

        titulo = self.request.GET.get("titulo", "").strip()
        veiculo_nome = self.request.GET.get("q", "").strip()
        estado = self.request.GET.get("estado", "").strip()
        cidade = self.request.GET.get("cidade", "").strip()

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if veiculo_nome:
            queryset = queryset.filter(cd_veiculo__nome_veiculo__icontains=veiculo_nome)

        if estado:
            queryset = queryset.filter(cd_veiculo__cd_uf=estado)

        if cidade:
            queryset = queryset.filter(cd_veiculo__id_municipio=cidade)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["estados"] = Uf.objects.all().order_by("nome_uf")  # Lista de estados
        return context
    
    def render_to_response(self, context, **response_kwargs):
        """Se for uma requisição via HTMX, renderiza apenas o conteúdo parcial."""
        if self.request.headers.get("HX-Request"):
            return render(self.request, "partials/noticia_list_partial.html", context)
        return super().render_to_response(context, **response_kwargs)
        
class NoticiaCreateView(CreateView):
    model = NoticiaImportada
    form_class = NoticiaForm
    template_name = "noticia_create.html"
    success_url = reverse_lazy("noticia_list")  # Volta para a lista após cadastrar

class NoticiaDetailView(DetailView):
    model = NoticiaImportada
    template_name = "partials/noticia_detail_partial.html"
    context_object_name = "noticia"

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get("HX-Request"):
            return render(self.request, "partials/noticia_detail_partial.html", context)
        return super().render_to_response(context, **response_kwargs)

def buscar_veiculos(request):
    query = request.GET.get("q", "").strip()
    
    if not query:
        return HttpResponse("")

    veiculos = Veiculosistemas.objects.filter(
        nome_veiculo__icontains=query
    ).values("cd_veiculo", "nome_veiculo")[:10]

    if not veiculos:
        return HttpResponse("<div class='dropdown-menu show'><li class='list-group-item disabled'>Nenhum veículo encontrado</li></div>")

    # Construindo HTML correto
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


def buscar_cidades(request):
    estado_id = request.GET.get("estado", "").strip()
    
    if not estado_id:
        return JsonResponse([], safe=False)  # Nenhum estado selecionado, retorna vazio

    cidades = Municipio.objects.filter(cd_uf=estado_id).values("id_municipio", "nome_municipio")

    return JsonResponse(list(cidades), safe=False)