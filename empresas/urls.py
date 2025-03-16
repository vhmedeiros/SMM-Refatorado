from django.urls import path
from . import views

urlpatterns = [
    path("empresas/list", views.EmpresaListView.as_view(), name="empresa_list"),
    path("empresas/create", views.EmpresaCreateView.as_view(), name="empresa_create"),
    path(
        "empresas/<str:pk>/detail",
        views.EmpresaDetailView.as_view(),
        name="empresa_detail",
    ),
    path(
        "empresas/<str:pk>/update",
        views.EmpresaUpdateView.as_view(),
        name="empresa_update",
    ),
]
