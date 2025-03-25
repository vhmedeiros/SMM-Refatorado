from django.contrib import admin
from .models import Categoriapalavrachave, Palavrachave

@admin.register(Categoriapalavrachave)
class CategoriaPalavraChaveAdmin(admin.ModelAdmin):
    list_display = ("nome", "id_cliente")
    list_filter = ("id_cliente",)
    search_fields = ("nome",)

@admin.register(Palavrachave)
class PalavraChaveAdmin(admin.ModelAdmin):
    list_display = ("palavra", "id_cliente", "id_categoria", "data_cadastro")
    list_filter = ("id_cliente", "id_categoria")
    search_fields = ("palavra",)
    ordering = ("-data_cadastro",)
    autocomplete_fields = ("id_cliente", "id_categoria")
