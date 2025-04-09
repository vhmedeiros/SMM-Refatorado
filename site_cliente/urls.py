from django.urls import path
from . import views

urlpatterns = [
    path("site/<str:sigla_cliente>", views.ClientePaginaPublicaView.as_view(), name="pagina_cliente"),
    path("site/<str:sigla_cliente>/<int:cd_noticia>/", views.ClienteNoticiaDetailView.as_view(), name="noticia_detail"),

]