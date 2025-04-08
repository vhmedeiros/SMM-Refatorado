from django import forms
from .models import NoticiaImportada
from veiculos.models import Veiculosistemas
from django.utils.timezone import now

class NoticiaForm(forms.ModelForm):
    # Campo do veículo (oculto, preenchido via popup)
    cd_veiculo = forms.ModelChoiceField(
        queryset=Veiculosistemas.objects.all(),
        widget=forms.HiddenInput(),
        required=True
    )

    class Meta:
        model = NoticiaImportada
        fields = [
            "cd_veiculo",
            "dt_noticia",
            "titulo",
            "subtitulo",
            "no_colunista",
            "id_editoria",
            "conteudo",
            "ds_url",
            "ds_url_media",
            "cd_pagina",
            "imagem"
        ]

        widgets = {
            "dt_noticia": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
            "no_colunista": forms.TextInput(attrs={"class": "form-control"}),
            "id_editoria": forms.Select(attrs={"class": "form-select"}),  # Usando Select ao invés de NumberInput
            "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "ds_url": forms.URLInput(attrs={"class": "form-control"}),
            "ds_url_media": forms.URLInput(attrs={"class": "form-control"}),
            "cd_pagina": forms.TextInput(attrs={"class": "form-control"}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

        labels = {
            "cd_veiculo": "Veículo",
            "dt_noticia": "Data da Notícia",
            "titulo": "Título",
            "subtitulo": "Subtítulo",
            "no_colunista": "Autor",
            "id_editoria": "Editoria",
            "conteudo": "Conteúdo",
            "ds_url": "URL da Notícia",
            "ds_url_media": "URL da Mídia",
            "cd_pagina": "Código da Página",
            "imagem": "Imagem",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Formata valor inicial da data
        if self.instance and self.instance.dt_noticia:
            self.fields["dt_noticia"].initial = self.instance.dt_noticia.strftime("%Y-%m-%dT%H:%M")

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Preenche dt_importacao apenas uma vez
        if not instance.dt_importacao:
            instance.dt_importacao = now()

        if commit:
            instance.save()
        return instance
