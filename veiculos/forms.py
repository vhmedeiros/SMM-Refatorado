from django import forms
from .models import Veiculosistemas


class VeiculoForm(forms.ModelForm):
    CHOICES_SIM_NAO = [("S", "Sim"), ("N", "Não")]

    # Campos para os dias da semana tratados como checkboxes
    in_domingo = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_segunda = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_terca = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_quarta = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_quinta = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_sexta = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )
    in_sabado = forms.BooleanField(
        required=False, widget=forms.CheckboxInput(attrs={"class": "form-check-input"})
    )

    class Meta:
        model = Veiculosistemas
        fields = [
            "nome_veiculo",
            "prioridade_veiculo",
            "veiculo_nacional",
            "situacao_veiculo",
            "ordem_veiculo",
            "cd_uf",
            "id_municipio",
            "cd_pais",
            "cd_lingua",
            "tipo_veiculo",
            "endereco_site_veiculo",
            "nome_identificador_url",
            "valor_publicitario_cm",
            "nome_referencia",
            "endereco_flip",
            "nome_url_stream",
            "in_domingo",
            "in_segunda",
            "in_terca",
            "in_quarta",
            "in_quinta",
            "in_sexta",
            "in_sabado",
            "situacao_url_stream",
            "quantidade_publico",
            "numero_telefone",
            "nome_endereco",
            "tolerancia_sem_noticia",
            "quantidade_min_noticia",
            "periodo_publicacao",
            "texto_comando_encoder",
            "cm_altura",
            "cm_largura",
            "json_lst_etiqueta",
            "in_extrair_texto_ocr",
        ]

        widgets = {
            "nome_veiculo": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nome do Veículo"}
            ),
            "prioridade_veiculo": forms.Select(
                attrs={"class": "form-select"}, choices=[("S", "Sim"), ("N", "Não")]
            ),
            "veiculo_nacional": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "situacao_veiculo": forms.Select(
                attrs={"class": "form-select"},
                choices=[("A", "Ativo"), ("I", "Inativo")],
            ),
            "ordem_veiculo": forms.Select(
                attrs={"class": "form-select"},
                choices=[(i, f"{i:02d} - Prioridade") for i in range(6)],
            ),
            "cd_uf": forms.Select(attrs={"class": "form-select"}),
            "id_municipio": forms.Select(attrs={"class": "form-select"}),
            "cd_pais": forms.Select(attrs={"class": "form-select"}),
            "cd_lingua": forms.Select(attrs={"class": "form-select"}),
            "tipo_veiculo": forms.Select(attrs={"class": "form-select"}),
            "endereco_site_veiculo": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "https://"}
            ),
            "nome_identificador_url": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "dominio.com"}
            ),
            "valor_publicitario_cm": forms.NumberInput(
                attrs={"class": "form-control", "step": 0.01, "placeholder": "R$"}
            ),
            "nome_referencia": forms.TextInput(attrs={"class": "form-control"}),
            "endereco_flip": forms.TextInput(attrs={"class": "form-control"}),
            "nome_url_stream": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "URL da Stream"}
            ),
            "situacao_url_stream": forms.TextInput(attrs={"class": "form-control"}),
            "quantidade_publico": forms.NumberInput(attrs={"class": "form-control"}),
            "numero_telefone": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "(XX) XXXXX-XXXX"}
            ),
            "nome_endereco": forms.TextInput(attrs={"class": "form-control"}),
            "tolerancia_sem_noticia": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "quantidade_min_noticia": forms.NumberInput(
                attrs={"class": "form-control"}
            ),
            "periodo_publicacao": forms.TextInput(attrs={"class": "form-control"}),
            "texto_comando_encoder": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "cm_altura": forms.NumberInput(
                attrs={"class": "form-control", "step": 0.01, "placeholder": "cm"}
            ),
            "cm_largura": forms.NumberInput(
                attrs={"class": "form-control", "step": 0.01, "placeholder": "cm"}
            ),
            "json_lst_etiqueta": forms.Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
            "in_extrair_texto_ocr": forms.Select(
                attrs={"class": "form-select"}, choices=[("S", "Sim"), ("N", "Não")]
            ),
        }

        labels = {
            "nome_veiculo": "Nome do Veículo",
            "prioridade_veiculo": "Prioridade do Veículo",
            "veiculo_nacional": "Veículo Nacional",
            "situacao_veiculo": "Situação do Veículo",
            "ordem_veiculo": "Ordem de Importância do Veículo",
            "cd_uf": "UF",
            "id_municipio": "Município",
            "cd_pais": "País",
            "cd_lingua": "Língua",
            "tipo_veiculo": "Tipo do Veículo",
            "endereco_site_veiculo": "Endereço do Site",
            "nome_identificador_url": "Identificador de URL (Domínio)",
            "valor_publicitario_cm": "Valor Publicitário (R$)",
            "nome_referencia": "Nome de Referência",
            "endereco_flip": "Endereço Flip",
            "nome_url_stream": "URL da Stream",
            "in_domingo": "Domingo",
            "in_segunda": "Segunda",
            "in_terca": "Terça",
            "in_quarta": "Quarta",
            "in_quinta": "Quinta",
            "in_sexta": "Sexta",
            "in_sabado": "Sábado",
            "situacao_url_stream": "Situação da URL Stream",
            "quantidade_publico": "Quantidade de Público",
            "numero_telefone": "Número de Telefone",
            "nome_endereco": "Endereço",
            "tolerancia_sem_noticia": "Tolerância sem Notícia",
            "quantidade_min_noticia": "Quantidade Mínima de Notícias",
            "periodo_publicacao": "Período de Publicação",
            "texto_comando_encoder": "Comando Encoder",
            "cm_altura": "Altura (cm)",
            "cm_largura": "Largura (cm)",
            "json_lst_etiqueta": "Etiquetas (JSON)",
            "in_extrair_texto_ocr": "Extrair Texto OCR",
        }

    def clean(self):
        cleaned_data = super().clean()

        # Corrige os valores para 'S' ou 'N' nos campos booleanos
        for dia in [
            "in_domingo",
            "in_segunda",
            "in_terca",
            "in_quarta",
            "in_quinta",
            "in_sexta",
            "in_sabado",
        ]:
            cleaned_data[dia] = "S" if cleaned_data.get(dia) else "N"

        return cleaned_data
