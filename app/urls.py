# from . import settings
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", include("autenticacao.urls")),
    path("", include("clientes.urls")),
    path("", include("configuracoes.urls")),
    path("", include("contratos.urls")),
    path("", include("emails.urls")),
    path("", include("empresas.urls")),
    path("", include("eventos.urls")),
    path("", include("noticias.urls")),
    path("", include("palavras_chave.urls", namespace="palavras_chave")),
    # path("", include("relatorios.urls")),
    path("", include("site_cliente.urls")),
    path("", include("veiculos.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
