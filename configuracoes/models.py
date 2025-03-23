from django.db import models
from clientes.models import ErpCliente
from empresas.models import ErpEmpresa
from django.utils.timezone import now

class ConfiguracaoCliente(models.Model):
    id_configuracao = models.AutoField(primary_key=True)  # PK real no banco de dados
    id_cliente = models.OneToOneField(
        ErpCliente, 
        on_delete=models.CASCADE, 
        verbose_name="Cliente",
        db_column="id_cliente", 
        related_name="configuracao"
    )
    nome_cliente_sistema = models.CharField(max_length=510, verbose_name="Nome no Sistema")
    empresa_prestadora = models.ForeignKey(
        ErpEmpresa, 
        on_delete=models.CASCADE, 
        verbose_name="Empresa Prestadora",
        db_column="id_empresa_prestadora"
    )
    sigla_cliente = models.CharField(max_length=10, verbose_name="Sigla do Cliente", db_column="sigla_cliente")
    url_pagina_cliente = models.CharField(
        max_length=255, null=True, blank=True, 
        verbose_name="URL da Página", db_column="url_pagina_cliente"
    )
    status_pagina = models.CharField(
        max_length=1, choices=[("A", "Ativo"), ("I", "Inativo")],
        verbose_name="Status da Página", db_column="status_pagina", default="I"
    )
    data_ativacao = models.DateTimeField(
        null=True, blank=True, verbose_name="Data de Ativação", 
        db_column="data_ativacao", default=now
    )
    logotipo = models.ImageField(upload_to="logos_clientes/", null=True, blank=True, verbose_name="Logotipo")
    cor_primaria = models.CharField(max_length=14, default="#000000", verbose_name="Cor Primária")
    cor_secundaria = models.CharField(max_length=14, default="#FFFFFF", verbose_name="Cor Secundária")

    class Meta:
        managed = False
        db_table = "configuracao_cliente"
        verbose_name = "Configuração do Cliente"
        verbose_name_plural = "Configurações do Cliente"

    def save(self, *args, **kwargs):
        """ Garante que id_cliente sempre seja preenchido corretamente. """
        if not self.id_cliente:
            raise ValueError("id_cliente é obrigatório antes de salvar.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nome_cliente_sistema} - {self.empresa_prestadora}"
