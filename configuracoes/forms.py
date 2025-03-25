from django import forms
from .models import ConfiguracaoCliente

class ConfiguracaoClienteForm(forms.ModelForm):
    class Meta:
        model = ConfiguracaoCliente
        fields = [
            "id_cliente",
            "nome_cliente_sistema",
            "sigla_cliente",
            "url_pagina_cliente",
            "status_pagina",
            "data_ativacao",
            "empresa_prestadora",
            "logotipo",
            "cor_primaria",
            "cor_secundaria",
        ]
        
        widgets = {
            "id_cliente": forms.HiddenInput(),
            "nome_cliente_sistema": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "sigla_cliente": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sigla do Cliente"}),
            "url_pagina_cliente": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL da Página"}),
            "status_pagina": forms.Select(choices=[("A", "Ativo"), ("I", "Inativo")], attrs={"class": "form-select"}),
            "data_ativacao": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "empresa_prestadora": forms.Select(attrs={"class": "form-select"}),
            "logotipo": forms.FileInput(attrs={"class": "form-control"}),
            "cor_primaria": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
            "cor_secundaria": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
        }

    def __init__(self, *args, **kwargs):
        id_cliente = kwargs.pop("id_cliente", None)
        super().__init__(*args, **kwargs)

        if id_cliente:
            self.fields["id_cliente"].initial = id_cliente

    def clean_id_cliente(self):
        """Garante que id_cliente nunca seja vazio."""
        id_cliente = self.cleaned_data.get("id_cliente")
        if not id_cliente:
            raise forms.ValidationError("O ID do cliente é obrigatório.")
        return id_cliente
