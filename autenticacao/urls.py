from django.urls import path
from .views import CustomLoginView, perfil, editar_perfil, UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path("login/", CustomLoginView.as_view(), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("perfil/", perfil, name='perfil'),
    path("perfil/editar/", editar_perfil, name='editar_perfil'),
    path("usuarios/list/", UsuarioListView.as_view(), name='usuario_list'),
    path("usuarios/novo/", UsuarioCreateView.as_view(), name='usuario_create'),
    path("usuarios/<int:pk>/editar/", UsuarioUpdateView.as_view(), name='usuario_update'),
    path("usuarios/<int:pk>/deletar/", UsuarioDeleteView.as_view(), name='usuario_delete'),

]