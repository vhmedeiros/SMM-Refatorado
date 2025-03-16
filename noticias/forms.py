from django import forms
from .models import NoticiaImportada


class NoticiaImportadaForm(forms.ModelForm):
    class Meta:
        model = NoticiaImportada
        fields = [
            "id_importacao",
            "dt_importacao",
            "dt_noticia",
            "titulo",
            "conteudo",
            "cd_veiculo",
            "ds_url",
            "subtitulo",
            "id_editoria",
            "no_colunista",
            "ds_url_media",
            "cd_pagina",
        ]
        widgets = {
            "id_importacao": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o ID da Importação",
                }
            ),
            "dt_importacao": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                    "placeholder": "Selecione a Data da Importação",
                }
            ),
            "dt_noticia": forms.DateTimeInput(
                attrs={
                    "class": "form-control",
                    "type": "datetime-local",
                    "placeholder": "Selecione a Data da Notícia",
                }
            ),
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o título da notícia",
                }
            ),
            "conteudo": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Digite o conteúdo da notícia aqui...",
                }
            ),
            "cd_veiculo": forms.Select(
                attrs={"class": "form-select", "placeholder": "Selecione o veículo"}
            ),
            "ds_url": forms.URLInput(
                attrs={"class": "form-control", "placeholder": "Cole a URL da notícia"}
            ),
            "subtitulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o subtítulo da notícia",
                }
            ),
            "id_editoria": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o ID da Editoria",
                }
            ),
            "no_colunista": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o nome do colunista",
                }
            ),
            "ds_url_media": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Cole a URL da mídia associada",
                }
            ),
            "cd_pagina": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Digite o código da página",
                }
            ),
        }
        labels = {
            "id_importacao": "ID da Importação",
            "dt_importacao": "Data da Importação",
            "dt_noticia": "Data da Notícia",
            "titulo": "Título",
            "conteudo": "Conteúdo",
            "cd_veiculo": "Veículo",
            "ds_url": "URL da Notícia",
            "subtitulo": "Subtítulo",
            "id_editoria": "ID da Editoria",
            "no_colunista": "Colunista",
            "ds_url_media": "URL da Mídia",
            "cd_pagina": "Código da Página",
        }


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = NoticiaImportada
        fields = ["titulo", "dt_noticia", "cd_veiculo"]
        widgets = {
            "dt_noticia": forms.DateInput(attrs={"type": "date"}),
        }