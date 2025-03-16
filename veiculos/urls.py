from django.urls import path
from . import views

urlpatterns = [
    # Listagem de Veículos
    path("veiculos/list/", views.VeiculoListView.as_view(), name="veiculo_list"),
    # Criação de Veículos
    path("veiculos/create/", views.VeiculoCreateView.as_view(), name="veiculo_create"),
    path(
        "veiculos/<int:pk>/detail/",
        views.VeiculoDetailView.as_view(),
        name="veiculo_detail",
    ),
    path(
        "veiculos/<int:pk>/update/",
        views.VeiculoUpdateView.as_view(),
        name="veiculo_update",
    ),
]
