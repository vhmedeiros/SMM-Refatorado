from django.contrib import admin
from .models import ErpCliente


@admin.register(ErpCliente)
class ErpClienteAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista do admin
    list_display = (
        "id_cliente",
        "nome_cliente",
        "numero_cnpj",
        "numero_cpf",
        "status_cliente",
        "data_cadastro",
    )
    # Campos que serão utilizados para busca
    search_fields = (
        "nome_cliente",
        "numero_cnpj",
        "numero_cpf",
        "nome_razao_social",
    )
    # Campos que podem ser filtrados
    list_filter = (
        "status_cliente",
        "cd_uf",
        "data_cadastro",
    )
    # Campos que podem ser editados diretamente na lista
    list_editable = ("status_cliente",)
    # Campos que organizam a visualização por data de cadastro
    date_hierarchy = "data_cadastro"
    # Configuração para exibição em colunas no formulário de edição
    fieldsets = (
        (
            "Informações Básicas",
            {
                "fields": (
                    "nome_cliente",
                    "nome_razao_social",
                    "numero_cnpj",
                    "numero_cpf",
                    "status_cliente",
                    "data_cadastro",
                )
            },
        ),
        (
            "Endereço",
            {
                "fields": (
                    "logradouro",
                    "complemento",
                    "bairro",
                    "numero_endereco",
                    "cep",
                    "cd_pais",
                    "cd_uf",
                    "id_municipio",
                )
            },
        ),
        (
            "Contato",
            {
                "fields": (
                    "telefone_gestor",
                    "email_gestor",
                    "contato_gestor",
                    "telefone_financeiro",
                    "email_financeiro",
                    "contato_financeiro",
                    "telefone_usuario",
                    "email_usuario",
                    "contato_usuario",
                )
            },
        ),
        (
            "Informações Adicionais",
            {
                "fields": (
                    "numero_inscricao_estadual",
                    "numero_inscricao_municipal",
                    "id_ultimo_servico_pago",
                )
            },
        ),
    )
