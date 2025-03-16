from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from unidecode import unidecode
from . import models, forms


class EmpresaListView(ListView):
    model = models.ErpEmpresa
    template_name = "empresa_list.html"
    context_object_name = "empresas"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_empresa = self.request.GET.get("nome_empresa")
        uf = self.request.GET.get("cd_uf")
        municipio = self.request.GET.get("id_municipio")

        if nome_empresa:
            nome_empresa_unaccented = unidecode(nome_empresa)
            queryset = queryset.filter(nome_empresa__icontains=nome_empresa_unaccented)

        if uf:
            queryset = queryset.filter(cd_uf=uf)

        if municipio:
            queryset = queryset.filter(id_municipio=municipio)

        return queryset


class EmpresaCreateView(CreateView):
    model = models.ErpEmpresa
    template_name = "empresa_create.html"
    form_class = forms.EmpresaForm
    success_url = reverse_lazy("empresa_list")


class EmpresaDetailView(DetailView):
    model = models.ErpEmpresa
    template_name = "empresa_detail.html"

    def get_object(self, queryset=None):
        try:
            obj = super().get_object(queryset)
            print(f"Detalhes da empresa: {obj}")
            return obj
        except models.ErpEmpresa.DoesNotExist:
            print(f"Empresa com pk={self.kwargs['pk']} não encontrada.")
            raise Http404("Empresa não encontrada.")


class EmpresaUpdateView(UpdateView):
    model = models.ErpEmpresa
    template_name = "empresa_update.html"
    form_class = forms.EmpresaForm
    success_url = reverse_lazy("empresa_list")
