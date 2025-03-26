from django.http import JsonResponse
from django.db.models import Q
from django.db.models.expressions import RawSQL
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from unidecode import unidecode
from . import models, forms


class VeiculoListView(ListView):

    # IMPORTANTE
    # pesquisar todos os veiculos pelo ID do veiculo

    model = models.Veiculosistemas
    template_name = "veiculo_list.html"
    context_object_name = "veiculos"
    paginate_by = 20

    def get_queryset(self):
        queryset = models.Veiculosistemas.objects.none()  # 🔹 Lista vazia por padrão
        nome_veiculo = self.request.GET.get("nome_veiculo")

        if nome_veiculo:  # 🔹 Só busca se houver um termo pesquisado
            queryset = super().get_queryset()

            if nome_veiculo.isdigit():  # 🔹 Se for número, busca pelo ID
                queryset = queryset.filter(cd_veiculo=nome_veiculo)
            else:
                nome_veiculo_normalizado = unidecode(nome_veiculo)  # 🔹 Remove acentos para busca
                queryset = queryset.annotate(
                    nome_sem_acento=RawSQL(
                        "dbo.RemoverAcentos(NmoVei)",
                        [],
                    )
                ).filter(
                    Q(nome_sem_acento__icontains=nome_veiculo_normalizado)  # 🔹 Busca sem acento
                    | Q(nome_veiculo__icontains=nome_veiculo)  # 🔹 Busca com acento
                )
        return queryset
class VeiculoCreateView(CreateView):
    model = models.Veiculosistemas
    template_name = "veiculo_create.html"
    form_class = forms.VeiculoForm
    success_url = reverse_lazy("veiculo_list")

    def form_valid(self, form):
        # Verificação e ajuste dos valores dos checkboxes
        dias_semana = [
            "in_domingo",
            "in_segunda",
            "in_terca",
            "in_quarta",
            "in_quinta",
            "in_sexta",
            "in_sabado",
        ]
        for dia in dias_semana:
            form.instance.__setattr__(dia, "S" if form.cleaned_data.get(dia) else "N")

        # Salva o objeto no banco de dados
        return super().form_valid(form)

    def form_invalid(self, form):
        # Debug para verificar os erros
        print("Formulário Inválido: ", form.errors)
        return super().form_invalid(form)


class VeiculoDetailView(DetailView):
    model = models.Veiculosistemas
    template_name = "veiculo_detail.html"


class VeiculoUpdateView(UpdateView):
    model = models.Veiculosistemas
    template_name = "veiculo_update.html"
    form_class = forms.VeiculoForm
    success_url = reverse_lazy("veiculo_list")


def buscar_municipios(request):
    """Retorna os municípios de uma UF específica"""
    cd_uf = request.GET.get("cd_uf")
    if cd_uf:
        municipios = models.Municipio.objects.filter(uf_municipio__cd_uf=cd_uf).values("id_municipio", "nome_municipio")
        return JsonResponse(list(municipios), safe=False)
    return JsonResponse([], safe=False)

