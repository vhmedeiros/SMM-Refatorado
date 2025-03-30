from django.db import models
from clientes.models import ErpCliente


class Categoriapalavrachave(models.Model):
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





# from django.db import models
# from noticias.models import NoticiaImportada
# from clientes.models import ErpCliente
# from palavras_chave.models import Categoriapalavrachave

# class VinculoNoticiaClienteCategoria(models.Model):
#     id_noticia = models.ForeignKey(
#         NoticiaImportada,
#         on_delete=models.CASCADE,
#         db_column='id_noticia',
#         verbose_name='Notícia'
#     )
#     id_cliente = models.ForeignKey(
#         ErpCliente,
#         on_delete=models.CASCADE,
#         db_column='id_cliente',
#         verbose_name='Cliente'
#     )
#     id_categoria = models.ForeignKey(
#         Categoriapalavrachave,
#         on_delete=models.CASCADE,
#         db_column='id_categoria',
#         verbose_name='Categoria'
#     )
#     data_vinculo = models.DateTimeField(
#         auto_now_add=True,
#         verbose_name='Data de Vínculo'
#     )

#     class Meta:
#         managed = False  # já existe no banco
#         db_table = 'VinculoNoticiaClienteCategoria'
#         unique_together = (('id_noticia', 'id_cliente', 'id_categoria'),)
#         verbose_name = 'Vínculo Notícia-Cliente-Categoria'
#         verbose_name_plural = 'Vínculos de Notícias com Clientes e Categorias'

#     def __str__(self):
#         return f"Notícia {self.id_noticia_id} → Cliente {self.id_cliente_id} / Categoria {self.id_categoria_id}"
