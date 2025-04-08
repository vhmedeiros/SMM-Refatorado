from django.contrib import admin
from .models import (
    EmailDisparo,
    EmailDestinatario,
    EmailDestinatarioBase,
    EmailHistoricoDisparo,
    EmailHorarioDisparo,
    EmailTemplatePadrao
)

# 🔁 Inline para editar horários diretamente no admin de EmailDisparo
class EmailHorarioDisparoInline(admin.TabularInline):
    model = EmailHorarioDisparo
    extra = 1
    verbose_name = "Horário de Disparo"
    verbose_name_plural = "Horários de Disparo"

# 📬 Admin do modelo principal de disparos
@admin.register(EmailDisparo)
class EmailDisparoAdmin(admin.ModelAdmin):
    list_display = ('id', 'assunto', 'id_cliente', 'id_categoria', 'status')
    list_filter = ('status',)
    search_fields = ('assunto',)
    readonly_fields = ('data_criacao', 'data_atualizacao')
    ordering = ('-data_criacao',)
    inlines = [EmailHorarioDisparoInline]  # permite adicionar horários diretamente no disparo

# 📩 Admin para visualização e edição de destinatários vinculados ao disparo
@admin.register(EmailDestinatario)
class EmailDestinatarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nome', 'tipo', 'ativo', 'enviar', 'id_email_disparo')
    list_editable = ('ativo', 'enviar')  # permite ativar ou desativar diretamente na lista
    list_filter = ('tipo', 'ativo', 'enviar')
    search_fields = ('email', 'nome')
    ordering = ('id_email_disparo', 'email')

# 📂 Admin dos destinatários base reutilizáveis por cliente
@admin.register(EmailDestinatarioBase)
class EmailDestinatarioBaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'nome', 'grupo', 'tipo', 'ativo', 'id_cliente')
    list_editable = ('grupo', 'tipo', 'ativo')
    list_filter = ('grupo', 'tipo', 'ativo')
    search_fields = ('email', 'nome', 'grupo')
    ordering = ('id_cliente', 'grupo', 'nome')

# 🕓 Histórico de cada disparo com status e retorno da API
@admin.register(EmailHistoricoDisparo)
class EmailHistoricoDisparoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_email_disparo', 'data_hora_agendada', 'data_hora_enviada', 'status')
    list_filter = ('status',)
    search_fields = ('status', 'mensagem_retorno', 'endpoint_enviado')
    ordering = ('-data_hora_enviada',)

# 🧩 Templates reutilizáveis de layout de e-mails
@admin.register(EmailTemplatePadrao)
class EmailTemplatePadraoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)
    ordering = ('nome',)
