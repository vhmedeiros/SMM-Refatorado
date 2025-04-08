from django.db import models
from clientes.models import ErpCliente
from palavras_chave.models import Categoriapalavrachave

# Constantes para escolhas
STATUS_CHOICES = [
    ('ATIVO', 'Ativo'),
    ('INATIVO', 'Inativo'),
]

TIPO_CHOICES = [
    ('PRINCIPAL', 'Principal'),
    ('CC', 'Com Cópia'),
    ('CCO', 'Com Cópia Oculta'),
]

# 🟢 Modelo principal que representa o disparo de um e-mail
class EmailDisparo(models.Model):
    id_cliente = models.ForeignKey(
        ErpCliente, on_delete=models.DO_NOTHING, db_column='id_cliente', verbose_name='Cliente'
    )
    id_categoria = models.ForeignKey(
        Categoriapalavrachave, on_delete=models.DO_NOTHING, db_column='id_categoria', verbose_name='Categoria'
    )
    assunto = models.CharField(max_length=255, verbose_name='Assunto')

    # Campos de personalização do layout do e-mail
    estilo_geral = models.TextField(blank=True, null=True, verbose_name='Estilo CSS Geral')
    cabecalho_html = models.TextField(blank=True, null=True, verbose_name='Cabeçalho HTML')
    rodape_html = models.TextField(blank=True, null=True, verbose_name='Rodapé HTML')
    titulo_html = models.TextField(blank=True, null=True, verbose_name='Template de Título da Notícia')

    # Controle de versão e status
    data_criacao = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    data_atualizacao = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    backup_ultima_configuracao = models.TextField(blank=True, null=True, verbose_name='Backup da Última Configuração')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO', verbose_name='Status')

    class Meta:
        managed = False
        db_table = 'EmailDisparo'
        verbose_name = 'Disparo de E-mail'
        verbose_name_plural = 'Disparos de E-mails'

    def __str__(self):
        return self.assunto


# 🧑‍💻 Representa um horário específico de disparo vinculado a um EmailDisparo
class EmailHorarioDisparo(models.Model):
    id_email_disparo = models.ForeignKey(
        EmailDisparo, on_delete=models.DO_NOTHING, db_column='id_email_disparo', verbose_name='Disparo'
    )
    dia_semana = models.IntegerField(choices=[
        (0, 'Segunda-feira'), (1, 'Terça-feira'), (2, 'Quarta-feira'),
        (3, 'Quinta-feira'), (4, 'Sexta-feira'), (5, 'Sábado'), (6, 'Domingo')
    ], verbose_name='Dia da Semana')
    horario = models.TimeField(verbose_name='Horário')

    class Meta:
        managed = False
        db_table = 'EmailHorarioDisparo'
        verbose_name = 'Horário de Disparo'
        verbose_name_plural = 'Horários de Disparo'

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.horario}"


# 📬 Histórico de envios relacionados a um disparo
class EmailHistoricoDisparo(models.Model):
    id_email_disparo = models.ForeignKey(
        EmailDisparo, on_delete=models.DO_NOTHING, db_column='id_email_disparo', verbose_name='Disparo'
    )
    data_hora_agendada = models.DateTimeField(verbose_name='Data/Hora Agendada', blank=True, null=True)
    data_hora_enviada = models.DateTimeField(verbose_name='Data/Hora Enviada', blank=True, null=True)
    status = models.CharField(max_length=100, verbose_name='Status do Envio')
    mensagem_retorno = models.TextField(blank=True, null=True, verbose_name='Mensagem da API')
    endpoint_enviado = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Endpoint Enviado')

    class Meta:
        managed = False
        db_table = 'EmailHistoricoDisparo'
        verbose_name = 'Histórico de Disparo de E-mail'
        verbose_name_plural = 'Histórico de Disparos de E-mail'

    def __str__(self):
        return f"Disparo {self.id_email_disparo_id} - {self.status}"


# 📐 Template padrão para o layout de e-mails (CSS, cabeçalho, rodapé etc.)
class EmailTemplatePadrao(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome do Modelo')
    estilo_geral = models.TextField(blank=True, null=True)
    cabecalho_html = models.TextField(blank=True, null=True)
    rodape_html = models.TextField(blank=True, null=True)
    titulo_html = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EmailTemplatePadrao'
        verbose_name = 'Template Padrão de E-mail'
        verbose_name_plural = 'Templates Padrão de E-mail'

    def __str__(self):
        return self.nome


# 📂 tabela base de destinatários reaproveitáveis por cliente
class EmailDestinatarioBase(models.Model):
    id_cliente = models.ForeignKey(
        ErpCliente, on_delete=models.DO_NOTHING, db_column='id_cliente', verbose_name='Cliente'
    )
    nome = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome do Destinatário')
    email = models.EmailField(verbose_name='E-mail')
    grupo = models.CharField(max_length=100, blank=True, null=True, verbose_name='Grupo do Destinatário')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name='Tipo')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')

    class Meta:
        managed = False
        db_table = 'EmailDestinatarioBase'
        verbose_name = 'Destinatário Base'
        verbose_name_plural = 'Destinatários Base'

    def __str__(self):
        return f"{self.nome or self.email} ({self.grupo or 'Sem grupo'})"


# 🚀 Ainda em uso nos disparos atuais (será substituído por cópia da base)
class EmailDestinatario(models.Model):
    id_email_disparo = models.ForeignKey(
        EmailDisparo, on_delete=models.DO_NOTHING, db_column='id_email_disparo', verbose_name='Disparo'
    )
    nome = models.CharField(max_length=255, blank=True, null=True, verbose_name='Nome do Destinatário')
    email = models.EmailField(verbose_name='E-mail')
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES, verbose_name='Tipo')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    enviar = models.BooleanField(default=True, verbose_name='Selecionado para envio')

    class Meta:
        managed = False
        db_table = 'EmailDestinatario'
        verbose_name = 'Destinatário de E-mail'
        verbose_name_plural = 'Destinatários de E-mail'

    def __str__(self):
        return self.email
