from django.test import TestCase

# Create your tests here.


# class NoticiaImportada(models.Model):
#     cd_noticia = models.AutoField(primary_key=True)
#     id_importacao = models.IntegerField(blank=True, null=True)
#     dt_importacao = models.DateTimeField()
#     dt_noticia = models.DateTimeField()
#     no_titulo = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
#     tt_noticia = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
#     id_veiculo = models.ForeignKey('Veiculosistemas', models.DO_NOTHING, db_column='id_veiculo')
#     ds_url = models.CharField(max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
#     tt_sutia = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     id_editoria = models.IntegerField(blank=True, null=True)
#     no_colunista = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     ds_url_media = models.CharField(max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     cd_pagina = models.CharField(max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     clientes_relacionados = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     categorias_relacionadas = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
#     processado = models.BooleanField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'noticia_importada'
