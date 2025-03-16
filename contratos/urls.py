from django.urls import path
from . import views

urlpatterns = [
    path(
        "contratos/cliente/<int:id_cliente>/",
        views.ErpContratosPorClienteListView.as_view(),
        name="contrato_list",
    ),
    path(
        "contratos/<int:pk>/detail/",
        views.ErpContratoDetailView.as_view(),
        name="contrato_detail",
    ),
    path(
        "contratos/<int:cliente_id>/create/",
        views.ErpContratoCreateView.as_view(),
        name="contrato_create",
    ),
    path(
        "contratos/<int:pk>/update/",
        views.ErpContratoUpdateView.as_view(),
        name="contrato_update",
    ),
]
