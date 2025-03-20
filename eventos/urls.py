from django.urls import path
from .views import EventoListView, EventoGlobalListView

urlpatterns = [
    path("clientes/<int:id_cliente>/eventos/", EventoListView.as_view(), name="eventos_cliente"),
    path("eventos/", EventoGlobalListView.as_view(), name="evento_global_list")
]
