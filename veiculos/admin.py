from django.contrib import admin
from .models import Lingua, Municipio, Uf, Pais, TipoVeiculo, Veiculosistemas


@admin.register(Lingua)
class LinguaAdmin(admin.ModelAdmin):
    list_display = ("cd_lingua", "nome_lingua")
    search_fields = ("cd_lingua", "nome_lingua")


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = (
        "id_municipio",
        "nome_municipio",
        "uf_municipio",
        "numero_latitude",
        "numero_longitude",
    )
    search_fields = ("id_municipio", "nome_municipio", "uf_municipio")
    list_filter = ("uf_municipio",)


@admin.register(Uf)
class UfAdmin(admin.ModelAdmin):
    list_display = ("cd_uf", "nome_uf", "nome_regiao", "cd_uf_ibge", "cd_pais")
    search_fields = ("cd_uf", "nome_uf", "nome_regiao")


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ("cd_pais", "nome_pais", "cd_pais_ibge")
    search_fields = ("cd_pais", "nome_pais")


@admin.register(TipoVeiculo)
class TipoVeiculoAdmin(admin.ModelAdmin):
    list_display = ("tipo_veiculo", "descricao_tipo_veiculo")
    search_fields = ("tipo_veiculo", "descricao_tipo_veiculo")


@admin.register(Veiculosistemas)
class VeiculosistemasAdmin(admin.ModelAdmin):
    list_display = (
        "cd_veiculo",
        "nome_veiculo",
        "cd_uf",
        "tipo_veiculo",
        "cd_pais",
        "id_municipio",
        "veiculo_nacional",
        "situacao_veiculo",
    )
    search_fields = (
        "cd_veiculo",
        "nome_veiculo",
        "cd_uf__nome_uf",
        "tipo_veiculo__descricao_tipo_veiculo",
        "cd_pais__nome_pais",
    )
    list_filter = (
        "cd_uf",
        "tipo_veiculo",
        "cd_pais",
        "veiculo_nacional",
        "situacao_veiculo",
    )
    raw_id_fields = ("cd_uf", "tipo_veiculo", "cd_pais", "id_municipio")
    list_per_page = 50
