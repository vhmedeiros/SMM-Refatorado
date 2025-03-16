from django.urls import path
from . import views

urlpatterns = [
    path("clientes/list", views.ClienteListView.as_view(), name="cliente_list"),
    path("clientes/create", views.ClienteCreateView.as_view(), name="cliente_create"),
    path("clientes/<int:pk>", views.ClienteDetailView.as_view(), name="cliente_detail"),
    path(
        "clientes/<int:pk>/update",
        views.ClienteUpdateView.as_view(),
        name="cliente_update",
    ),
]
