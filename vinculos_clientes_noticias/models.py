from django.db import models
from noticias.models import NoticiaImportada
from clientes.models import ErpCliente
from palavras_chave.models import Categoriapalavrachave


class VinculoNoticiaClienteCategoria(models.Model):
    cd_noticia = models.ForeignKey(
        NoticiaImportada,
        on_delete=models.CASCADE,
        db_column='cd_noticia',
        verbose_name='Notícia',
        related_name='vinculos_noticias'
    )
    id_cliente = models.ForeignKey(
        ErpCliente,
        on_delete=models.CASCADE,
        db_column='id_cliente',
        verbose_name='Cliente',
        related_name='vinculos_clientes'
    )
    id_categoria = models.ForeignKey(
        Categoriapalavrachave,
        on_delete=models.CASCADE,
        db_column='id_categoria',
        verbose_name='Categoria',
        related_name='vinculos_categorias'
    )
    data_vinculo = models.DateTimeField(auto_now_add=True, verbose_name="Data de Vínculo")
    dt_processamento = models.DateTimeField(null=True, blank=True, verbose_name="Data de Processamento")

    class Meta:
        db_table = 'VinculoNoticiaClienteCategoria'
        verbose_name = 'Vínculo Notícia-Cliente-Categoria'
        verbose_name_plural = 'Vínculos Notícia-Cliente-Categoria'
        unique_together = ('cd_noticia', 'id_cliente', 'id_categoria')
        managed = False

    def __str__(self):
        return f"Notícia {self.cd_noticia_id} - Cliente {self.id_cliente_id} - Categoria {self.id_categoria_id}"


class JobLogExecucao(models.Model):
    nome_job = models.CharField(max_length=255, verbose_name="Nome do Job")
    status = models.CharField(max_length=100, verbose_name="Status")  # Ex: Sucesso, Erro
    mensagem = models.TextField(blank=True, null=True, verbose_name="Mensagem de Log")
    data_execucao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Execução")

    class Meta:
        managed = False
        db_table = "JobLogExecucao"
        verbose_name = "Log de Execução do Job"
        verbose_name_plural = "Logs de Execução de Jobs"

    def __str__(self):
        return f"{self.nome_job} - {self.status} em {self.data_execucao.strftime('%d/%m/%Y %H:%M')}"