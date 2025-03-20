from django.urls import path
from . import views

urlpatterns = [
    path("configuracoes/cliente/", views.ClienteConfigListView.as_view(), name="config_cliente_list"),
    # path("configuracoes/cliente/<int:pk>/", views.ClienteConfigDetailView.as_view(), name="config_cliente_detail"),
    path("configuracoes/cliente/<int:pk>/editar/", views.ClienteConfigUpdateView.as_view(), name="config_cliente_updat1e"),
    path("configuracoes/cliente/<int:id_cliente>/visual-create/", views.ClienteConfigVisualCreateView.as_view(), name="config_cliente_visual_create"),
    path("configuracoes/cliente/<int:pk>/visual-update/", views.ClienteConfigVisualUpdateView.as_view(), name="config_cliente_visual_update"),
    path("configuracoes/cliente/<int:id_cliente>/redirect/", views.config_cliente_redirect, name="config_cliente_redirect"),
]
