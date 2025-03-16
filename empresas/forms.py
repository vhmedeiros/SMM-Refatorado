from django import forms
from .models import ErpEmpresa


class EmpresaForm(forms.ModelForm):
    STATUS_EMPRESA_CHOICES = [
        ("A", "Ativo"),
        ("D", "Desabilitado"),
    ]

    SMI_GERACAO_CHOICES = [
        ("S", "Sim"),
        ("N", "Não"),
    ]

    st_empresa = forms.ChoiceField(
        choices=STATUS_EMPRESA_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
        label="Status da Empresa",
    )

    in_smi_gerar_servico_contrato = forms.ChoiceField(
        choices=SMI_GERACAO_CHOICES,
        widget=forms.Select(
            attrs={
                "class": "form-select",
            }
        ),
        label="SMI Geração de Serviço Contrato",
    )

    class Meta:
        model = ErpEmpresa
        fields = [
            "cd_empresa",
            "numero_cnpj",
            "nome_empresa",
            "nome_razao_social",
            "nome_fantasia",
            "numero_insc_estadual",
            "numero_reg_contab",
            "nome_endereco",
            "nome_logradouro",
            "nome_complemento",
            "nome_bairro",
            "numero_endereco",
            "numero_cep",
            "cd_pais",
            "sg_uf",
            "id_municipio",
            "numero_telefone_nf",
            "numero_telefone",
            "st_empresa",
            "nome_email_administrativo",
            "nome_email_geral",
            "nome_email_from",
            "nome_email_replyto",
            "nome_dominio_smi",
            "nome_dominio_cliente",
            "nome_email_proposta",
            "path_personalizacao",
            "cd_cnae",
            "info_complementar",
            "numero_serie_atual_nf",
            "tipo_ambiente_nf",
            "descricao_natureza_operacao",
            "valor_aliquota_issqn",
            "cd_servico_issqn",
            "cd_regime_tributacao",
            "numero_insc_municipal",
            "tipo_servico_nf",
            "cd_regime_tributario",
            "nome_email_contador",
            "in_smi_gerar_servico_contrato",
            "in_force_https",
        ]
        widgets = {
            "cd_empresa": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Código da Empresa"}
            ),
            "numero_cnpj": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o CNPJ"}
            ),
            "nome_empresa": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Nome da Empresa",
                }
            ),
            "nome_razao_social": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite a Razão Social"}
            ),
            "nome_fantasia": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Nome Fantasia"}
            ),
            "numero_insc_estadual": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a Inscrição Estadual",
                }
            ),
            "numero_reg_contab": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Registro Contábil",
                }
            ),
            "nome_endereco": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Endereço"}
            ),
            "nome_logradouro": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Logradouro"}
            ),
            "nome_complemento": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Complemento"}
            ),
            "nome_bairro": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Bairro"}
            ),
            "numero_endereco": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Número do Endereço",
                }
            ),
            "numero_cep": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o CEP"}
            ),
            "cd_pais": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Código do País",
                }
            ),
            "sg_uf": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite a UF"}
            ),
            "id_municipio": forms.Select(
                attrs={"class": "form-select", "placeholder": "Selecione o Município"}
            ),
            "numero_telefone_nf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Telefone para Nota Fiscal",
                }
            ),
            "numero_telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Telefone"}
            ),
            "nome_email_administrativo": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o E-mail Administrativo",
                }
            ),
            "nome_email_geral": forms.EmailInput(
                attrs={"class": "form-control", "placeholder": "Digite o E-mail Geral"}
            ),
            "nome_email_from": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o E-mail de Origem",
                }
            ),
            "nome_email_replyto": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o E-mail de Resposta",
                }
            ),
            "nome_dominio_smi": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Domínio SMI"}
            ),
            "nome_dominio_cliente": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Domínio do Cliente",
                }
            ),
            "nome_email_proposta": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o E-mail para Propostas",
                }
            ),
            "path_personalizacao": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Caminho de Personalização",
                }
            ),
            "cd_cnae": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o CNAE"}
            ),
            "info_complementar": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Digite Informações Complementares",
                }
            ),
            "numero_serie_atual_nf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Número de Série Atual (NF)",
                }
            ),
            "tipo_ambiente_nf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Tipo de Ambiente (NF)",
                }
            ),
            "descricao_natureza_operacao": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a Natureza da Operação",
                }
            ),
            "valor_aliquota_issqn": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a Alíquota ISSQN",
                }
            ),
            "cd_servico_issqn": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite o Serviço ISSQN"}
            ),
            "cd_regime_tributacao": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Regime de Tributação",
                }
            ),
            "numero_insc_municipal": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite a Inscrição Municipal",
                }
            ),
            "tipo_servico_nf": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Tipo de Serviço (NF)",
                }
            ),
            "cd_regime_tributario": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o Regime Tributário",
                }
            ),
            "nome_email_contador": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o E-mail do Contador",
                }
            ),
            "in_force_https": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Digite se Forçar HTTPS"}
            ),
        }
        labels = {
            "cd_empresa": "Código da Empresa",
            "numero_cnpj": "CNPJ",
            "nome_empresa": "Nome da Empresa",
            "nome_razao_social": "Razão Social",
            "nome_fantasia": "Nome Fantasia",
            "numero_insc_estadual": "Inscrição Estadual",
            "numero_reg_contab": "Registro Contábil",
            "nome_endereco": "Endereço",
            "nome_logradouro": "Logradouro",
            "nome_complemento": "Complemento",
            "nome_bairro": "Bairro",
            "numero_endereco": "Número do Endereço",
            "numero_cep": "CEP",
            "cd_pais": "País",
            "sg_uf": "UF",
            "id_municipio": "Município",
            "numero_telefone_nf": "Telefone NF",
            "numero_telefone": "Telefone",
            "st_empresa": "Status da Empresa",
            "nome_email_administrativo": "E-mail Administrativo",
            "nome_email_geral": "E-mail Geral",
            "nome_email_from": "E-mail de Origem",
            "nome_email_replyto": "E-mail de Resposta",
            "nome_dominio_smi": "Domínio SMI",
            "nome_dominio_cliente": "Domínio do Cliente",
            "nome_email_proposta": "E-mail para Propostas",
            "path_personalizacao": "Caminho de Personalização",
            "cd_cnae": "CNAE",
            "info_complementar": "Informações Complementares",
            "numero_serie_atual_nf": "Número de Série Atual (NF)",
            "tipo_ambiente_nf": "Tipo de Ambiente (NF)",
            "descricao_natureza_operacao": "Natureza da Operação",
            "valor_aliquota_issqn": "Alíquota ISSQN",
            "cd_servico_issqn": "Serviço ISSQN",
            "cd_regime_tributacao": "Regime de Tributação",
            "numero_insc_municipal": "Inscrição Municipal",
            "tipo_servico_nf": "Tipo de Serviço (NF)",
            "cd_regime_tributario": "Regime Tributário",
            "nome_email_contador": "E-mail do Contador",
            "in_smi_gerar_servico_contrato": "SMI Geração de Serviço Contrato",
            "in_force_https": "Forçar HTTPS",
        }
