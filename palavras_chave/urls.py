from django.urls import path
from . import views

app_name = "palavras_chave"

urlpatterns = [
    path("configuracoes/cliente/<int:id_cliente>/categorias/", views.CategoriaListView.as_view(), name="categoria_list"),
    path("configuracoes/cliente/<int:id_cliente>/categorias/nova/", views.CategoriaCreateView.as_view(), name="categoria_create"),
    path("configuracoes/categorias/<int:pk>/editar/", views.CategoriaUpdateView.as_view(), name="categoria_update"),
    path("configuracoes/categorias/<int:pk>/excluir/", views.CategoriaDeleteView.as_view(), name="categoria_delete"),

    # palavras-chave
    
    path('configuracoes/cliente/<int:id_cliente>/categorias/<int:id_categoria>/palavras/nova/', views.PalavraChaveCreateView.as_view(), name='palavra_chave_create'),
    path('configuracoes/palavras/<int:pk>/editar/', views.PalavraChaveUpdateView.as_view(), name='palavra_chave_update'),
    path('configuracoes/palavras/<int:pk>/excluir/', views.PalavraChaveDeleteView.as_view(), name='palavra_chave_delete'),

]