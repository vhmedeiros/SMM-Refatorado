from django.urls import path
from . import views

urlpatterns = [
    path("noticias/list/", views.NoticiaListView.as_view(), name="noticia_list"),
    path("noticias/create/", views.NoticiaCreateView.as_view(), name="noticia_create"),
    path(
        "noticias/<int:pk>/detail/",
        views.NoticiaDetailView.as_view(),
        name="noticia_detail",
    ),
#     path(
#         "noticias/<int:pk>/update/",
#         views.NoticiaUpdateView.as_view(),
#         name="noticia_update",
#     ),
    path("buscar-veiculos/", views.buscar_veiculos, name="buscar_veiculos"),
    path("buscar-cidades/", views.buscar_cidades, name="buscar_cidades"),
]
