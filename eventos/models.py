from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from clientes.models import ErpCliente

class Evento(models.Model):
    id_evento = models.AutoField(primary_key=True, verbose_name="ID do Evento")  # 🔹 Chave primária do evento
    id_cliente = models.ForeignKey(ErpCliente, on_delete=models.CASCADE, db_column="id_cliente", verbose_name="Cliente", related_name="eventos", null=True, blank=True)  # 🔹 Relacionamento opcional com Cliente (nem todo evento precisa ter um cliente vinculado)
    descricao = models.CharField(db_column="descricao", max_length=255, verbose_name="Descrição do Evento")  # 🔹 Texto descritivo do evento
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, db_column="id_usuario", null=True, blank=True, verbose_name="Usuário", related_name="eventos_registrados")  # 🔹 Usuário que realizou a ação
    data_hora = models.DateTimeField(db_column="data_hora", auto_now_add=True, verbose_name="Data e Hora do Evento")  # 🔹 Data e hora do evento
    
    # 🔥 Suporte para eventos globais (registro de mudanças em qualquer modelo)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, db_column="content_type_id", verbose_name="Modelo Relacionado")  # 🔹 Define qual modelo está sendo referenciado
    object_id = models.PositiveIntegerField(db_column="object_id", verbose_name="ID do Objeto Relacionado")  # 🔹 ID do registro afetado
    objeto = GenericForeignKey("content_type", "object_id")  # 🔹 Cria a relação genérica com qualquer tabela do banco
    acao = models.CharField(db_column="acao", max_length=20, choices=[("criado", "Criado"), ("atualizado", "Atualizado"), ("excluído", "Excluído")], verbose_name="Ação Realizada")  # 🔹 Tipo da ação executada

    class Meta:
        managed = False  # 🔹 Indica que a tabela já existe no banco de dados e não deve ser gerenciada pelo Django
        db_table = "evento"  # 🔹 Define o nome correto da tabela no SQL Server
        ordering = ["-data_hora"]  # 🔹 Ordena os eventos do mais recente para o mais antigo

    def __str__(self):
        return f"{self.get_acao_display()} - {self.descricao} ({self.data_hora})"
