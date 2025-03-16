from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("autenticacao.urls")),
    path("", include("clientes.urls")),
    # path("", include("configuracoes.urls")),
    path("", include("contratos.urls")),
    # path("", include("emails.urls")),
    path("", include("empresas.urls")),
    path("", include("noticias.urls")),
    # path("", include("relatorios.urls")),
    path("", include("veiculos.urls")),
]
