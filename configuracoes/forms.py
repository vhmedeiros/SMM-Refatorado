from django import forms
from .models import ConfiguracaoCliente
from datetime import datetime

class ConfiguracaoClienteForm(forms.ModelForm):
    class Meta:
        model = ConfiguracaoCliente
        fields = [
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
            "nome_cliente_sistema": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),
            "sigla_cliente": forms.TextInput(attrs={"class": "form-control", "placeholder": "Sigla do Cliente"}),
            "url_pagina_cliente": forms.TextInput(attrs={"class": "form-control", "placeholder": "URL da Página do Cliente"}),
            "status_pagina": forms.Select(choices=[("A", "Ativo"), ("I", "Inativo")], attrs={"class": "form-select"}),
            "data_ativacao": forms.TextInput(attrs={"class": "form-control", "readonly": "readonly"}),  # Mantém leitura apenas
            "empresa_prestadora": forms.Select(attrs={"class": "form-select"}),
            "logotipo": forms.FileInput(attrs={"class": "form-control"}),
            "cor_primaria": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
            "cor_secundaria": forms.TextInput(attrs={"class": "form-control", "type": "color"}),
        }

        labels = {
            "sigla_cliente": "Sigla do Cliente",
            "url_pagina_cliente": "URL da Página do Cliente",
            "status_pagina": "Status da Página",
            "data_ativacao": "Data de Ativação",
            "empresa_prestadora": "Empresa Prestadora",
            "logotipo": "Logotipo",
            "cor_primaria": "Cor Primária",
            "cor_secundaria": "Cor Secundária",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Se a página do cliente estiver ativa e não tiver data, define a data atual
        if self.instance and self.instance.status_pagina == "A":
            if isinstance(self.instance.data_ativacao, str):
                try:
                    data_ativacao = datetime.strptime(self.instance.data_ativacao, "%Y-%m-%d %H:%M:%S")
                except ValueError:
                    data_ativacao = datetime.now()  # Se falhar, usa data atual
            else:
                data_ativacao = self.instance.data_ativacao or datetime.now()

            self.fields["data_ativacao"].initial = data_ativacao.strftime("%d/%m/%Y %H:%M:%S")

    def clean_data_ativacao(self):
        """Atualiza a data de ativação automaticamente caso a página seja ativada."""
        status = self.cleaned_data.get("status_pagina")
        data_ativacao = self.cleaned_data.get("data_ativacao")

        if status == "A" and not data_ativacao:
            return datetime.now()

        return data_ativacao
