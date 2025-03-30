from django.db import models
from veiculos.models import Veiculosistemas


class NoticiaImportada(models.Model):
    cd_noticia = models.AutoField(primary_key=True)
    id_importacao = models.IntegerField(null=True, blank=True)
    dt_importacao = models.DateTimeField()
    dt_noticia = models.DateTimeField()
    titulo = models.CharField(
        db_column="no_titulo",
        max_length=500,
    )
    conteudo = models.CharField(
        max_length=4000,
        db_column="tt_noticia",
    )
    cd_veiculo = models.ForeignKey(
        Veiculosistemas, models.DO_NOTHING, db_column="id_veiculo"
    )
    ds_url = models.CharField(
        max_length=500, blank=True, null=True
    )
    subtitulo = models.CharField(
        db_column="tt_sutia", max_length=1000, blank=True, null=True
    )
    id_editoria = models.IntegerField(blank=True, null=True)
    no_colunista = models.CharField(max_length=1000, blank=True, null=True)
    ds_url_media = models.CharField(max_length=2000, blank=True, null=True)
    cd_pagina = models.CharField(max_length=6, blank=True, null=True)
    imagem = models.ImageField(upload_to="noticias/", blank=True, null=True, verbose_name="Imagem")

    class Meta:
        managed = False
        db_table = "noticia_importada"
        verbose_name_plural = "Notícias Importadas"
        ordering = ["-dt_noticia"]

    def __str__(self):
        return self.titulo
