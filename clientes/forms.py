from django import forms
from .models import ErpCliente


class ClienteForm(forms.ModelForm):
    STATUS_CLIENTE = [
        ("A", "Ativo"),
        ("E", "Excluído"),
    ]

    status_cliente = forms.ChoiceField(
        choices=STATUS_CLIENTE,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Status Cliente",
    )

    class Meta:
        model = ErpCliente
        fields = [
            "numero_cnpj",
            "numero_cpf",
            "nome_cliente",
            "nome_razao_social",
            "numero_inscricao_estadual",
            "numero_inscricao_municipal",
            "endereco",
            "logradouro",
            "numero_endereco",
            "complemento",
            "bairro",
            "cd_pais",
            "cd_uf",
            "id_municipio",
            "cep",
            "telefone_gestor",
            "email_gestor",
            "contato_gestor",
            "contato_financeiro",
            "telefone_financeiro",
            "email_financeiro",
            "contato_usuario",
            "telefone_usuario",
            "email_usuario",
            "status_cliente",
            "data_cadastro",
            "id_ultimo_servico_pago",
        ]

        widgets = {
            "numero_cnpj": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número CNPJ",
                }
            ),
            "numero_cpf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número CPF",
                }
            ),
            "nome_cliente": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome Cliente",
                }
            ),
            "nome_razao_social": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Nome Razão Social",
                }
            ),
            "numero_inscricao_estadual": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número Inscrição Estadual",
                }
            ),
            "numero_inscricao_municipal": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número Inscrição Municipal",
                }
            ),
            "endereco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Endereço",
                }
            ),
            "logradouro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Logradouro",
                }
            ),
            "numero_endereco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Número Endereço",
                }
            ),
            "complemento": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Complemento",
                }
            ),
            "bairro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Bairro",
                }
            ),
            "cd_pais": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "País",
                }
            ),
            "cd_uf": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Estado",
                }
            ),
            "id_municipio": forms.Select(
                attrs={
                    "class": "form-control",
                    "placeholder": "Município",
                }
            ),
            "cep": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "CEP",
                }
            ),
            "telefone_gestor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Telefone Gestor",
                }
            ),
            "email_gestor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Gestor",
                }
            ),
            "contato_gestor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contato Gestor",
                }
            ),
            "contato_financeiro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contato Financeiro",
                }
            ),
            "telefone_financeiro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Telefone Financeiro",
                }
            ),
            "email_financeiro": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Financeiro",
                }
            ),
            "contato_usuario": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Contato Usuário",
                }
            ),
            "telefone_usuario": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Telefone Usuário",
                }
            ),
            "email_usuario": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Usuário",
                }
            ),
            "status_cliente": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            "data_cadastro": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                    "placeholder": "Data Cadastro",
                }
            ),
            "id_ultimo_servico_pago": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "ID Último Serviço Pago",
                }
            ),
        }
        labels = {
            "numero_cnpj": "Número CNPJ",
            "numero_cpf": "Número CPF",
            "nome_cliente": "Nome Cliente",
            "nome_razao_social": "Nome Razão Social",
            "numero_inscricao_estadual": "Número Inscrição Estadual",
            "numero_inscricao_municipal": "Número Inscrição Municipal",
            "endereco": "Endereço",
            "logradouro": "Logradouro",
            "numero_endereco": "Número Endereço",
            "complemento": "Complemento",
            "bairro": "Bairro",
            "cd_pais": "Código País",
            "cd_uf": "Código UF",
            "id_municipio": "ID Município",
            "cep": "CEP",
            "telefone_gestor": "Telefone Gestor",
            "email_gestor": "Email Gestor",
            "contato_gestor": "Contato Gestor",
            "contato_financeiro": "Contato Financeiro",
            "telefone_financeiro": "Telefone Financeiro",
            "email_financeiro": "Email Financeiro",
            "contato_usuario": "Contato Usuário",
            "telefone_usuario": "Telefone Usuário",
            "email_usuario": "Email Usuário",
            "status_cliente": "Status Cliente",
            "data_cadastro": "Data Cadastro",
            "id_ultimo_servico_pago": "ID Último Serviço Pago",
        }
