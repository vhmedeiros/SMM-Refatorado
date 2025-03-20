from django.shortcuts import get_object_or_404, redirect
from django.db import connection
from datetime import datetime
from django.utils.timezone import now, localtime
from django.urls import reverse_lazy
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

class ClienteConfigVisualCreateView(CreateView):
    model = ConfiguracaoCliente
    form_class = ConfiguracaoClienteForm
    template_name = "config_cliente_visual_update.html"

    def get_initial(self):
        """Define valores iniciais para o formulário com base no cliente selecionado."""
        id_cliente = self.kwargs.get("id_cliente")
        cliente = get_object_or_404(ErpCliente, pk=id_cliente)
        return {
            "id_cliente": cliente,
            "nome_cliente_sistema": cliente.nome_cliente,  # Ajuste conforme o campo real do cliente
        }

    def form_valid(self, form):
        """Salva a configuração e redireciona para a página de edição."""
        self.object = form.save()
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

def config_cliente_redirect(request, id_cliente):
    """
    Redireciona para a página correta:
    - Se a configuração já existir, redireciona para o update.
    - Se não existir, redireciona para a criação de uma nova.
    """
    request.session["id_cliente"] = int(id_cliente)
    try:
        # Verifica se já existe uma configuração para o cliente
        config = ConfiguracaoCliente.objects.get(id_cliente=id_cliente)
        return redirect("config_cliente_visual_update", pk=config.id_cliente.pk)
    except ConfiguracaoCliente.DoesNotExist:
        # Se não existir, redireciona para criar uma nova configuração
        return redirect("config_cliente_visual_create", id_cliente=id_cliente)