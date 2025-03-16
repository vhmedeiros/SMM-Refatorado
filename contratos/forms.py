from django import forms
from .models import ErpContrato


class ErpContratoForm(forms.ModelForm):
    class Meta:
        model = ErpContrato
        exclude = ["id_cliente"]  # 'id_cliente' será excluído do formulário
        # Não é necessário incluir 'fields' se você está usando 'exclude'.
        widgets = {
            "data_inicio_vigencia": forms.DateInput(
                attrs={"type": "date", "placeholder": "dd/mm/yyyy"}
            ),
            "data_fim_vigencia": forms.DateInput(
                attrs={"type": "date", "placeholder": "dd/mm/yyyy"}
            ),
            "data_cadastro": forms.DateTimeInput(
                attrs={"type": "datetime-local", "placeholder": "dd/mm/yyyy hh:mm:ss"}
            ),
            "descricao_objeto": forms.Textarea(
                attrs={
                    "rows": 5,
                    "cols": 20,
                    "placeholder": "Descrição do objeto do contrato",
                }
            ),
            "informacao_adicional": forms.Textarea(
                attrs={"rows": 5, "cols": 20, "placeholder": "Informações adicionais"}
            ),
            "tipo_prorrogacao": forms.Select(
                choices=[  # Corrigido de 'choises' para 'choices'
                    ("ANO", "Anual"),
                    ("MES", "Mensal"),
                    ("AUT", "Automático"),
                    ("TRI", "Trimestral"),
                    ("SEM", "Semestral"),
                    ("NAO", "Não Prorrogar"),
                ]
            ),
            "status_contrato": forms.Select(
                choices=[
                    ("A", "Ativo"),
                    ("I", "Inativo"),
                ]
            ),
            "tipo_cobranca": forms.Select(
                choices=[
                    ("MES", "Mensal"),
                    ("ANO", "Anual"),
                    ("OUT", "Outro"),
                ]
            ),
            "forma_envio_nf": forms.Select(
                choices=[
                    ("A", "Email Automático"),
                    ("M", "Email Manual"),
                    ("C", "Correios"),
                    ("O", "Outro"),
                ]
            ),
            # 'in_contrato_assinado': forms.BooleanField(
            #     widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            #     initial=True,  # Marca a caixa de seleção como marcada por padrão
            # ),
        }
        labels = {  # Corrigido de 'lables' para 'labels'
            "cd_empresa": "Empresa",
            "cd_identificacao": "Identificação",
            "descricao_contrato": "Descrição",
            "data_inicio_vigencia": "Início da Vigência",
            "data_fim_vigencia": "Fim da Vigência",
            "tipo_prorrogacao": "Prorrogação",
            "descricao_objeto": "Objeto",
            "informacao_adicional": "Informações Adicionais",
            "valor_contrato": "Valor",
            "dia_emissao_nota_fiscal": "Dia de Emissão da NF",
            "status_contrato": "Status",
            "in_contrato_assinado": "Contrato Assinado",
            "tipo_cobranca": "Tipo de Cobrança",
            "data_cadastro": "Data de Cadastro",
            "dia_do_pagamento": "Dia do Pagamento",
            "dia_aviso_fim_vigencia": "Dia de Aviso de Fim de Vigência",
            "forma_envio_nf": "Forma de Envio da NF",
        }
