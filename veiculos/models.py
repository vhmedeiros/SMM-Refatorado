"""
ERRO DE CODIFICAÇÃO UTF-16

ao gerar o models pelo inspectdb, eles estão vindo com padrão UTF-16.
isso da um bug e não é possível executar o django. Portanto,
deve forçar a geração dos models com o comando:

py manage.py inspectdb lingua municipio uf pais tipo_veiculo VeiculoSistemas | Out-File -Encoding utf8 veiculos/models.py


e depois deve deixar o padrão apenas como UTF-8.
"""

from django.db import models


class Lingua(models.Model):
    cd_lingua = models.CharField(
        primary_key=True, max_length=2, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    nome_lingua = models.CharField(
        db_column="no_lingua",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "lingua"

    def __str__(self):
        return self.cd_lingua


class Uf(models.Model):
    cd_uf = models.CharField(
        db_column="sg_uf",
        primary_key=True,
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    nome_uf = models.CharField(
        db_column="no_uf", max_length=50, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    nome_regiao = models.CharField(
        db_column="no_regiao",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    cd_uf_ibge = models.SmallIntegerField(blank=True, null=True)
    cd_pais = models.CharField(
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    id_capital = models.SmallIntegerField(blank=True, null=True)
    numero_gmt = models.CharField(
        db_column="nr_gmt",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "uf"

    def __str__(self):
        return self.cd_uf


class Municipio(models.Model):
    id_municipio = models.IntegerField(primary_key=True)
    id_mesorregiao = models.SmallIntegerField()
    uf_municipio = models.ForeignKey(Uf, models.PROTECT, db_column="uf_municipio")
    nome_municipio = models.CharField(
        db_column="no_municipio",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    numero_latitude = models.FloatField(db_column="nr_latitude", blank=True, null=True)
    numero_longitude = models.FloatField(
        db_column="nr_longitude", blank=True, null=True
    )
    id_municipio_ibge = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "municipio"

    def __str__(self):
        return self.nome_municipio


class Pais(models.Model):
    cd_pais = models.CharField(
        primary_key=True, max_length=6, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    nome_pais = models.CharField(
        db_column="no_pais", max_length=100, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    cd_pais_ibge = models.CharField(
        max_length=50, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )

    class Meta:
        managed = False
        db_table = "pais"
        verbose_name_plural = "País"

    def __str__(self):
        return self.nome_pais


class TipoVeiculo(models.Model):
    tipo_veiculo = models.CharField(
        db_column="tp_veiculo",
        primary_key=True,
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )
    descricao_tipo_veiculo = models.CharField(
        db_column="ds_tipo_veiculo",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
    )

    class Meta:
        managed = False
        db_table = "tipo_veiculo"
        verbose_name_plural = "Tipos de veículos"

    def __str__(self):
        return self.descricao_tipo_veiculo


class Veiculosistemas(models.Model):
    cd_veiculo = models.AutoField(db_column="CodVei", primary_key=True)
    codsys = models.IntegerField(db_column="CodSys", blank=True, null=True)
    nome_veiculo = models.CharField(
        db_column="NmoVei", max_length=510, db_collation="SQL_Latin1_General_CP1_CI_AS"
    )
    prioridade_veiculo = models.CharField(
        db_column="PriVei",
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    veiculo_nacional = models.BooleanField(
        db_column="VeiNacional", blank=True, null=True
    )
    ordem_veiculo = models.IntegerField(db_column="VeiOrdem", blank=True, null=True)
    codtipovei = models.IntegerField(db_column="CodTipoVei", blank=True, null=True)
    cd_uf = models.ForeignKey(
        Uf, models.DO_NOTHING, db_column="sg_uf", blank=True, null=True
    )
    tipo_veiculo = models.ForeignKey(
        TipoVeiculo, models.DO_NOTHING, db_column="tp_veiculo"
    )
    situacao_veiculo = models.CharField(
        db_column="st_veiculo",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    endereco_site_veiculo = models.CharField(
        db_column="end_veiculo",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    nome_identificador_url = models.CharField(
        db_column="no_identificador_url",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    data_ultima_noticia = models.DateTimeField(
        db_column="dt_ultima_noticia", blank=True, null=True
    )
    cd_usuario_web = models.CharField(
        db_column="cd_usuario_web",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    cd_senha_web = models.CharField(
        db_column="cd_senha_web",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    cd_pais = models.ForeignKey(Pais, models.DO_NOTHING, db_column="cd_pais")
    cd_lingua = models.ForeignKey(
        Lingua, models.DO_NOTHING, db_column="cd_lingua", blank=True, null=True
    )
    valor_publicitario_cm = models.DecimalField(
        db_column="vl_publicitario_cm",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    cd_usuario_flip = models.CharField(
        db_column="cd_usuario_flip",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    cd_senha_flip = models.CharField(
        db_column="cd_senha_flip",
        max_length=60,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    nome_referencia = models.CharField(
        db_column="no_referencia",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    endereco_flip = models.CharField(
        db_column="end_flip",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    id_municipio = models.ForeignKey(
        Municipio, models.DO_NOTHING, db_column="id_municipio", blank=True, null=True
    )
    nome_url_stream = models.CharField(
        db_column="no_url_stream",
        max_length=4000,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_domingo = models.CharField(
        db_column="in_domingo",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_segunda = models.CharField(
        db_column="in_segunda",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_terca = models.CharField(
        db_column="in_terca",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_quarta = models.CharField(
        db_column="in_quarta",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_quinta = models.CharField(
        db_column="in_quinta",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_sexta = models.CharField(
        db_column="in_sexta",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_sabado = models.CharField(
        db_column="in_sabado",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    situacao_url_stream = models.CharField(
        db_column="st_url_stream",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    quantidade_publico = models.IntegerField(
        db_column="qt_publico", blank=True, null=True
    )
    numero_telefone = models.CharField(
        db_column="nr_telefone",
        max_length=30,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    nome_endereco = models.CharField(
        db_column="no_endereco",
        max_length=300,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    data_atualizacao = models.DateField(
        db_column="dt_atualizacao", blank=True, null=True
    )
    tolerancia_sem_noticia = models.IntegerField(
        db_column="tolerancia_sem_noticia", blank=True, null=True
    )
    quantidade_min_noticia = models.IntegerField(
        db_column="qt_min_noticia", blank=True, null=True
    )
    periodo_publicacao = models.CharField(
        db_column="periodo_publicacao",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    texto_comando_encoder = models.CharField(
        db_column="tt_comando_encoder",
        max_length=2000,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    cm_altura = models.DecimalField(
        db_column="cm_altura", max_digits=6, decimal_places=2, blank=True, null=True
    )
    cm_largura = models.DecimalField(
        db_column="cm_largura", max_digits=6, decimal_places=2, blank=True, null=True
    )
    json_lst_etiqueta = models.TextField(
        db_column="json_lst_etiqueta",
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )
    in_extrair_texto_ocr = models.CharField(
        db_column="in_extrair_texto_ocr",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
    )

    class Meta:
        managed = False
        db_table = "VeiculoSistemas"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return self.nome_veiculo
