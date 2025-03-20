from django.views.generic import ListView
from .models import Evento
from clientes.models import ErpCliente

class EventoListView(ListView):
    model = Evento
    template_name = "evento_list.html"
    context_object_name = "eventos"

    def get_queryset(self):
        id_cliente = self.kwargs.get("id_cliente")
        return Evento.objects.filter(id_cliente=id_cliente).order_by("-data_hora")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente"] = ErpCliente.objects.get(pk=self.kwargs["id_cliente"])
        return context


class EventoGlobalListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'
    paginate_by = 20