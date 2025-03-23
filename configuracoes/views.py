from django.shortcuts import get_object_or_404, redirect
from django.db import connection
from datetime import datetime
from django.utils.timezone import now, localtime
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from clientes.models import ErpCliente
from contratos.models import ErpContrato
from empresas.models import ErpEmpresa
from clientes.forms import ClienteForm
from .models import ConfiguracaoCliente
from .forms import ConfiguracaoClienteForm

class ClienteConfigListView(ListView):
    model = ErpCliente
    template_name = "config_cliente_list.html"
    context_object_name = "clientes"
    paginate_by = 50

    def get_queryset(self):
        queryset = ErpCliente.objects.none()  # Não exibir clientes por padrão
        nome_cliente = self.request.GET.get("nome_cliente")
        buscar_todos = self.request.GET.get("buscar_todos")

        if nome_cliente or buscar_todos:
            queryset = ErpCliente.objects.all()
            if nome_cliente:
                queryset = queryset.filter(nome_cliente__icontains=nome_cliente)
            if not buscar_todos:
                queryset = queryset.filter(status_cliente="A")

        # Adicionar a empresa prestadora ao queryset
        for cliente in queryset:
            contrato = ErpContrato.objects.filter(id_cliente=cliente).first()
            cliente.empresa_prestadora = contrato.cd_empresa.nome_fantasia if contrato else "-"

        return queryset

# class ClienteConfigVisualCreateView(CreateView):
#     model = ConfiguracaoCliente
#     form_class = ConfiguracaoClienteForm
#     template_name = "config_cliente_visual_update.html"

#     def get_form_kwargs(self):
#         """Passa o id_cliente explicitamente no form."""
#         kwargs = super().get_form_kwargs()
#         id_cliente = self.kwargs.get("id_cliente")
#         cliente = get_object_or_404(ErpCliente, pk=id_cliente)
#         kwargs["initial"] = {
#             "id_cliente": cliente, 
#             "nome_cliente_sistema": cliente.nome_cliente,
#         }
#         return kwargs

#     def form_valid(self, form):
#         """Força a associação correta do id_cliente antes de salvar."""
#         id_cliente = self.kwargs.get("id_cliente")  
#         cliente = get_object_or_404(ErpCliente, pk=id_cliente)  

#         # Define manualmente o id_cliente no formulário antes do salvamento
#         form.instance.id_cliente = cliente  

#         # Salva corretamente
#         self.object = form.save(commit=False)  
#         self.object.id_cliente = cliente  # Garante que o ID seja preenchido
#         self.object.save()

#         return redirect("config_cliente_visual_update", pk=self.object.id_cliente.pk)

class ClienteConfigVisualCreateView(CreateView):
    model = ConfiguracaoCliente
    form_class = ConfiguracaoClienteForm
    template_name = "config_cliente_visual_update.html"

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        id_cliente = self.kwargs.get("id_cliente")

        if id_cliente:
            cliente = get_object_or_404(ErpCliente, pk=id_cliente)
            kwargs["id_cliente"] = cliente.id_cliente
            kwargs.setdefault("initial", {})["id_cliente"] = cliente.id_cliente
            kwargs.setdefault("initial", {})["nome_cliente_sistema"] = cliente.nome_cliente

        return kwargs

    def form_valid(self, form):
        id_cliente = self.kwargs.get("id_cliente")
        cliente = get_object_or_404(ErpCliente, pk=id_cliente)

        form.instance.id_cliente = cliente
        form.instance.nome_cliente_sistema = cliente.nome_cliente

        self.object = form.save(commit=False)
        self.object.save()

        return redirect("config_cliente_visual_update", pk=self.object.id_cliente.pk)

class ClienteConfigDetailView(DetailView):
    model = ErpCliente
    template_name = "config_cliente_detail.html"
    context_object_name = "cliente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente_selecionado"] = self.object
        context["configuracao"] = ConfiguracaoCliente.objects.filter(id_cliente=self.object).first()
        return context
class ClienteConfigUpdateView(UpdateView):
    model = ErpCliente
    template_name = "config_cliente_update.html"
    form_class = ClienteForm
    success_url = reverse_lazy("config_cliente_list")

class ClienteConfigVisualUpdateView(UpdateView):
    model = ConfiguracaoCliente
    form_class = ConfiguracaoClienteForm
    template_name = "config_cliente_visual_update.html"

    def get_object(self):
        id_cliente = self.kwargs.get("pk")
        obj = get_object_or_404(ConfiguracaoCliente, id_cliente=id_cliente)

        # Ajusta a data de ativação para o horário local
        if obj.data_ativacao:
            obj.data_ativacao = localtime(obj.data_ativacao)

        return obj

    def form_valid(self, form):
        self.object = form.save()
        return redirect("config_cliente_detail", pk=self.object.id_cliente.pk)

# def config_cliente_redirect(request, id_cliente):
#     """
#     Redireciona para a página correta:
#     - Se a configuração já existir, redireciona para o update.
#     - Se não existir, redireciona para a criação de uma nova.
#     """
#     request.session["id_cliente"] = int(id_cliente)
#     try:
#         # Verifica se já existe uma configuração para o cliente
#         config = ConfiguracaoCliente.objects.get(id_cliente=id_cliente)
#         return redirect("config_cliente_visual_update", pk=config.id_cliente.pk)
#     except ConfiguracaoCliente.DoesNotExist:
#         # Se não existir, redireciona para criar uma nova configuração
#         return redirect("config_cliente_visual_create", id_cliente=id_cliente)


def config_cliente_redirect(request, id_cliente):
    request.session["id_cliente"] = int(id_cliente)

    if ConfiguracaoCliente.objects.filter(id_cliente=id_cliente).exists():
        return redirect("config_cliente_visual_update", pk=id_cliente)

    return redirect(reverse("config_cliente_visual_create", kwargs={"id_cliente": id_cliente}))