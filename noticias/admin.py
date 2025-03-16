from django.contrib import admin
from .models import NoticiaImportada
from veiculos.models import Veiculosistemas


@admin.register(NoticiaImportada)
class NoticiaImportadaAdmin(admin.ModelAdmin):
    # Configuração dos campos que aparecerão na listagem
    list_display = (
        "cd_noticia",
        "titulo",
        "dt_noticia",
        "cd_veiculo",
    )
    # Campos para busca rápida
    search_fields = (
        "titulo",
        "no_colunista",
        "ds_url",
        "subtitulo",
    )

    # Filtros laterais
    list_filter = (
        "dt_noticia",
        "cd_veiculo",
        "id_editoria",
    )

    # Ordenação padrão
    ordering = ("-dt_noticia",)

    # Campos de edição no Django Admin
    fieldsets = (
        (
            "Informações Gerais",
            {
                "fields": (
                    "titulo",
                    "subtitulo",
                    "conteudo",
                    "cd_veiculo",
                    "id_editoria",
                )
            },
        ),
        (
            "Datas e Importação",
            {"fields": ("id_importacao", "dt_importacao", "dt_noticia")},
        ),
        (
            "Detalhes Adicionais",
            {"fields": ("no_colunista", "ds_url", "ds_url_media", "cd_pagina")},
        ),
    )
