from django.db import models
from clientes.models import ErpCliente


class Categoriapalavrachave(models.Model):
    # categoria = models.AutoField(primary_key=True, db_column="id")
    id_cliente = models.ForeignKey(
        ErpCliente, models.DO_NOTHING, db_column="id_cliente", verbose_name="Cliente")
    nome = models.CharField(
        unique=True, max_length=255, db_collation="SQL_Latin1_General_CP1_CI_AS", verbose_name="Nome da Categoria"
    )
    status = models.BooleanField(
        default=True, verbose_name="Status"
    )

    class Meta:
        managed = False
        db_table = "CategoriaPalavraChave"
        verbose_name = "Categoria"
    def __str__(self):
        return self.nome


class Palavrachave(models.Model):
    id_cliente = models.ForeignKey(
        ErpCliente, models.DO_NOTHING, db_column="id_cliente", verbose_name="Cliente"
    )
    id_categoria = models.ForeignKey(
        Categoriapalavrachave, models.DO_NOTHING, db_column="id_categoria", verbose_name="Categoria"
    )
    palavra = models.CharField(
        max_length=255, db_collation="SQL_Latin1_General_CP1_CI_AS", verbose_name="Palavra-Chave"
    )
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    status = models.BooleanField(
        default=True, verbose_name="Status"
    )

    class Meta:
        managed = False
        db_table = "PalavraChave"
        unique_together = (("palavra", "id_cliente", "id_categoria"),)
        verbose_name = "Palavra-Chave"
        verbose_name_plural = "Palavras-Chave"

    def __str__(self):
        return self.palavra


