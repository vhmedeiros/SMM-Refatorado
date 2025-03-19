# from django import forms
# from .models import NoticiaImportada
# from veiculos.models import Veiculosistemas


# class NoticiaForm(forms.ModelForm):
#     class Meta:
#         model = NoticiaImportada
#         fields = [
#             "cd_veiculo", "titulo", "subtitulo", "conteudo", "ds_url",
#             "dt_noticia", "id_importacao", "dt_importacao", "id_editoria",
#             "no_colunista", "ds_url_media", "cd_pagina", "imagem"
#         ]
        
#         widgets = {
#             "cd_veiculo": forms.Select(attrs={"class": "form-select"}),
#             "titulo": forms.TextInput(attrs={"class": "form-control"}),
#             "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
#             "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
#             "ds_url": forms.URLInput(attrs={"class": "form-control"}),
#             "dt_noticia": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
#             "id_importacao": forms.NumberInput(attrs={"class": "form-control"}),
#             "dt_importacao": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
#             "id_editoria": forms.NumberInput(attrs={"class": "form-control"}),
#             "no_colunista": forms.TextInput(attrs={"class": "form-control"}),
#             "ds_url_media": forms.URLInput(attrs={"class": "form-control"}),
#             "cd_pagina": forms.TextInput(attrs={"class": "form-control"}),
#             "imagem": forms.FileInput(attrs={"class": "form-control"}),
#         }

#         labels = {
#             "cd_veiculo": "Veículo",
#             "titulo": "Título",
#             "subtitulo": "Subtítulo",
#             "conteudo": "Conteúdo",
#             "ds_url": "URL da Notícia",
#             "dt_noticia": "Data da Notícia",
#             "id_importacao": "ID da Importação",
#             "dt_importacao": "Data de Importação",
#             "id_editoria": "ID da Editoria",
#             "no_colunista": "Colunista",
#             "ds_url_media": "URL da Mídia",
#             "cd_pagina": "Código da Página",
#             "imagem": "Imagem",
#         }

from django import forms
from .models import NoticiaImportada
from veiculos.models import Veiculosistemas

class NoticiaForm(forms.ModelForm):
    cd_veiculo = forms.ModelChoiceField(
        queryset=Veiculosistemas.objects.all(),
        widget=forms.HiddenInput(),
        required=True
    )

    class Meta:
        model = NoticiaImportada
        fields = [
            "cd_veiculo", "dt_importacao", "dt_noticia", "titulo", "conteudo",
            "ds_url", "subtitulo", "id_editoria", "no_colunista", "ds_url_media",
            "cd_pagina", "clientes_relacionados", "categorias_relacionadas", "imagem"
        ]
        
        widgets = {
            "dt_importacao": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "dt_noticia": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"},
                format="%Y-%m-%dT%H:%M"
            ),
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "conteudo": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "ds_url": forms.URLInput(attrs={"class": "form-control"}),
            "subtitulo": forms.TextInput(attrs={"class": "form-control"}),
            "id_editoria": forms.NumberInput(attrs={"class": "form-control"}),
            "no_colunista": forms.TextInput(attrs={"class": "form-control"}),
            "ds_url_media": forms.URLInput(attrs={"class": "form-control"}),
            "cd_pagina": forms.TextInput(attrs={"class": "form-control"}),
            "clientes_relacionados": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "categorias_relacionadas": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "imagem": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

        labels = {
            "cd_veiculo": "Veículo",
            "dt_importacao": "Data de Cadastro",
            "dt_noticia": "Data de Publicação",
            "titulo": "Título",
            "conteudo": "Conteúdo",
            "ds_url": "URL da Notícia",
            "subtitulo": "Subtítulo",
            "id_editoria": "ID da Editoria",
            "no_colunista": "Colunista",
            "ds_url_media": "URL da Mídia",
            "cd_pagina": "Código da Página",
            "clientes_relacionados": "Clientes Relacionados",
            "categorias_relacionadas": "Categorias Relacionadas",
            "imagem": "Imagem",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 🔹 Veículo: Campo exibível no formulário, mas enviando o ID correto
        self.fields["veiculo_nome"] = forms.CharField(
            widget=forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Digite ou selecione um veículo",
                "id": "veiculo-autocomplete"
            }),
            required=False
        )

        # 🔹 Se já existir uma data, formata corretamente para aparecer no campo
        if self.instance and self.instance.dt_importacao:
            self.fields["dt_importacao"].initial = self.instance.dt_importacao.strftime("%Y-%m-%dT%H:%M")
        if self.instance and self.instance.dt_noticia:
            self.fields["dt_noticia"].initial = self.instance.dt_noticia.strftime("%Y-%m-%dT%H:%M")
