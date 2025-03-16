from django.contrib import admin
from django.utils.html import format_html
from .models import ErpContrato, ErpProduto


@admin.register(ErpContrato)
class ErpContratoAdmin(admin.ModelAdmin):
    list_display = (
        "id_contrato",
        "id_cliente",
        "cd_empresa",
        "descricao_contrato",
        "data_inicio_vigencia",
        "data_fim_vigencia",
        "tipo_prorrogacao",
        "descricao_objeto",
        "informacao_adicional",
        "valor_contrato",
        "dia_emissao_nota_fiscal",
        "status_contrato",
        "in_contrato_assinado",
        "tipo_cobranca",
        "data_cadastro",
        "dia_do_pagamento",
        "dia_aviso_fim_vigencia",
        "forma_envio_nf",
    )
    search_fields = (
        "id_contrato",
        "id_cliente",
        "cd_empresa",
        "descricao_contrato",
        "data_inicio_vigencia",
        "data_fim_vigencia",
        "tipo_prorrogacao",
        "descricao_objeto",
        "informacao_adicional",
        "valor_contrato",
        "dia_emissao_nota_fiscal",
        "status_contrato",
    )
    list_per_page = 50


class SubProdutosInline(admin.TabularInline):
    model = ErpProduto
    fk_name = "cd_produto_principal"
    extra = 1
    verbose_name = "Subproduto"
    verbose_name_plural = "Subprodutos"


@admin.register(ErpProduto)
class ErpProdutoAdmin(admin.ModelAdmin):
    list_display = (
        "cd_produto",
        "descricao",
        "situacao_produto",
        "cd_produto_principal",
    )
    list_filter = ("situacao_produto",)
    search_fields = ("descricao",)
    autocomplete_fields = ("cd_produto_principal",)
    inlines = [SubProdutosInline]
    filter_horizontal = ("veiculos",)
    ordering = ("cd_produto",)

    def cd_produto_principal_display(self, obj):
        return obj.cd_produto_principal.descricao if obj.cd_produto_principal else "-"

    cd_produto_principal_display.short_description = "Produto Principal"

    def view_on_site(self, obj):
        return (
            format_html('<a href="{}"> Ver no site</a>', obj.get_absolute_url())
            if hasattr(obj, "get_absolute_url")
            else None
        )
