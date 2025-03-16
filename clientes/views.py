from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from . import models, forms


class ClienteListView(ListView):
    model = models.ErpCliente
    template_name = "cliente_list.html"
    context_object_name = "clientes"
    paginate_by = 50

    def get_queryset(self):
        queryset = super().get_queryset()
        nome_cliente = self.request.GET.get("nome_cliente")

        if nome_cliente:
            queryset = queryset.filter(nome_cliente__icontains=nome_cliente)

        return queryset


class ClienteCreateView(CreateView):
    model = models.ErpCliente
    template_name = "cliente_create.html"
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente_list")


class ClienteDetailView(DetailView):
    model = models.ErpCliente
    template_name = "cliente_detail.html"
    context_object_name = "cliente"


class ClienteUpdateView(UpdateView):
    model = models.ErpCliente
    template_name = "cliente_update.html"
    form_class = forms.ClienteForm
    success_url = reverse_lazy("cliente_list")
