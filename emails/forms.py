from django import forms
from .models import EmailDisparo, EmailHorarioDisparo, EmailDestinatario, EmailDestinatarioBase
from palavras_chave.models import Categoriapalavrachave
from django.forms.models import inlineformset_factory

class EmailDisparoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        cliente = kwargs.pop('cliente', None) # cliente é passado pela view
        super().__init__(*args, **kwargs)

        # # Força o campo de categoria (alguns campos somem quando o model é managed=False)
        # self.fields['id_categoria'] = forms.ModelChoiceField(
        #     queryset=Categoriapalavrachave.objects.all(),
        #     required=True,
        #     empty_label="Selecione uma categoria",
        #     widget=forms.Select(attrs={'class': 'form-select'})
        # )

        # categorias
        self.fields['categorias'] = forms.ModelMultipleChoiceField(
            queryset=Categoriapalavrachave.objects.none() if not cliente else Categoriapalavrachave.objects.filter(id_cliente=cliente).distinct(),
            widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
            required=False,
            label='Categorias Vinculadas',
        )

    class Meta:
        model = EmailDisparo
        fields = [
            'categorias',
            'assunto',
            'estilo_geral',
            'cabecalho_html',
            'rodape_html',
            'titulo_html',
            'status',
        ]
        labels = {
            'categorias': 'Categorias Vinculadas',
            'assunto': 'Assunto',
            'estilo_geral': 'Estilo CSS Geral',
            'cabecalho_html': 'Cabeçalho HTML',
            'rodape_html': 'Rodapé HTML',
            'titulo_html': 'Template de Título da Notícia',
            'status': 'Status',
        }
        widgets = {
            'assunto': forms.TextInput(attrs={'class': 'form-control'}),
            'estilo_geral': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cabecalho_html': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'rodape_html': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'titulo_html': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class EmailHorarioDisparoForm(forms.ModelForm):
    class Meta:
        model = EmailHorarioDisparo
        fields = ['dia_semana', 'horario']
        labels = {
            'dia_semana': 'Dia da Semana',
            'horario': 'Horário'
        }
        widgets = {
            'dia_semana': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
        }

EmailDestinatarioFormSet = inlineformset_factory(
    EmailDisparo,
    EmailDestinatario,
    fields=["nome", "email", "tipo", "ativo"],
    extra=1,
    can_delete=True,
    widgets={
        'nome': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'tipo': forms.Select(attrs={'class': 'form-select'}),
        'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'})
    },
    labels={
        'nome': 'Nome do Destinatário',
        'email': 'E-mail',
        'tipo': 'Tipo',
        'ativo': 'Ativo'
    }
)

class EmailDestinatarioBaseForm(forms.ModelForm):
    """
    Formulário para cadastro e edição de destinatários base.
    Permite reaproveitamento por cliente e agrupamento por setor (grupo).
    """
    class Meta:
        model = EmailDestinatarioBase
        fields = [
            'nome',
            'email',
            'grupo',
            'tipo',
            'ativo'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'grupo': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# importar CSV
class EmailDestinatarioBaseCSVForm(forms.Form):
    """
    Formulário para importar destinatários de um arquivo CSV.
    """
    csv_file = forms.FileField(label='Arquivo CSV', required=True, widget=forms.ClearableFileInput(attrs={'accept': '.csv'}))

    def clean_csv_file(self):
        csv_file = self.cleaned_data.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError("O arquivo deve ser no formato CSV.")
        return csv_file

# form para Destinatarios dos disparos
class EmailDestinatarioForm(forms.ModelForm):
    """
    Formulário para criação e edição de destinatários vinculados a um disparo de e-mail específico.
    Esses destinatários são únicos por disparo e podem ser personalizados manualmente.
    """

    class Meta:
        model = EmailDestinatario
        fields = ['nome', 'email', 'tipo', 'ativo', 'enviar']
        labels = {
            'nome': 'Nome do Destinatário',
            'email': 'E-mail',
            'tipo': 'Tipo de Envio',
            'ativo': 'Destinatário Ativo',
            'enviar': 'Marcar para envio',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: João Silva'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: joao@email.com'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'enviar': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_email(self):
        """
        Validação básica do campo de e-mail para garantir unicidade por disparo (caso necessário no futuro).
        """
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("O e-mail é obrigatório.")
        return email
