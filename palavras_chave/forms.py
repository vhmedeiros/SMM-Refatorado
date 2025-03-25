from django import forms
from .models import Categoriapalavrachave, Palavrachave


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoriapalavrachave
        fields = ["nome", "status"]

        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nome da Categoria"}),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }

        labels = {
            "nome": "Nome da Categoria",
            "status": "Categoria Ativa",
        }


# class PalavraChaveForm(forms.ModelForm):
#     class Meta:
#         model = Palavrachave
#         fields = ['palavra', 'status']

#     def __init__(self, *args, **kwargs):
#         self.id_categoria = kwargs.pop('id_categoria', None)
#         super().__init__(*args, **kwargs)

#     def clean_palavra(self):
#         palavra = self.cleaned_data['palavra']
#         if Palavrachave.objects.filter(palavra__iexact=palavra, id_categoria=self.id_categoria).exists():
#             raise forms.ValidationError("Esta palavra já está cadastrada nesta categoria.")
#         return palavra

class PalavraChaveForm(forms.ModelForm):
    STATUS_CHOICES = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label="Status"
    )

    class Meta:
        model = Palavrachave
        fields = ['palavra', 'status']