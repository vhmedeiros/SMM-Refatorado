from django.contrib import admin
from .models import ErpEmpresa


@admin.register(ErpEmpresa)
class ErpEmpresaAdmin(admin.ModelAdmin):
    # Campos exibidos na listagem
    list_display = (
        "cd_empresa",
        "numero_cnpj",
        "nome_empresa",
        "nome_razao_social",
        "nome_fantasia",
        "st_empresa",
        "sg_uf",
        "id_municipio",
    )
    # Campos que podem ser clicados para abrir detalhes
    list_display_links = ("cd_empresa", "nome_empresa")

    # Campos de busca
    search_fields = (
        "cd_empresa",
        "numero_cnpj",
        "nome_empresa",
        "nome_razao_social",
        "nome_fantasia",
    )

    # Filtros laterais
    list_filter = (
        "sg_uf",
        "st_empresa",
        "id_municipio",
    )

    # Ordenação padrão (por código da empresa, decrescente)
    ordering = ("-cd_empresa",)

    # Campos editáveis diretamente na listagem
    list_editable = ("st_empresa",)

    # Campos exibidos na página de detalhes
    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": (
                    "cd_empresa",
                    "numero_cnpj",
                    "nome_empresa",
                    "nome_razao_social",
                    "nome_fantasia",
                )
            },
        ),
        (
            "Localização",
            {
                "fields": (
                    "nome_endereco",
                    "nome_logradouro",
                    "nome_complemento",
                    "nome_bairro",
                    "numero_endereco",
                    "numero_cep",
                    "sg_uf",
                    "id_municipio",
                )
            },
        ),
        (
            "Contato",
            {
                "fields": (
                    "numero_telefone",
                    "numero_telefone_nf",
                    "nome_email_administrativo",
                    "nome_email_geral",
                    "nome_email_from",
                    "nome_email_replyto",
                )
            },
        ),
        (
            "Configurações",
            {
                "fields": (
                    "st_empresa",
                    "cd_cnae",
                    "info_complementar",
                    "in_smi_gerar_servico_contrato",
                    "in_force_https",
                )
            },
        ),
    )

    # Limitação de registros por página
    list_per_page = 20
