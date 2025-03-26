from django.db import models
from veiculos.models import Municipio


class ErpEmpresa(models.Model):
    cd_empresa = models.CharField(
        primary_key=True,
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Código da Empresa",
    )
    numero_cnpj = models.CharField(
        db_column="nr_cnpj",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="CNPJ",
    )
    nome_empresa = models.CharField(
        db_column="no_empresa",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Nome da Empresa",
    )
    nome_razao_social = models.CharField(
        db_column="no_razao_social",
        max_length=300,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Razão Social",
    )
    nome_fantasia = models.CharField(
        db_column="no_fantasia",
        max_length=300,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Nome Fantasia",
    )
    numero_insc_estadual = models.CharField(
        db_column="nr_insc_estadual",
        max_length=13,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Inscrição Estadual",
    )
    numero_reg_contab = models.CharField(
        db_column="nr_reg_contab",
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Registro Contábil",
    )
    nome_endereco = models.CharField(
        db_column="no_endereco",
        max_length=1000,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Endereço",
    )
    nome_logradouro = models.CharField(
        db_column="no_logradouro",
        max_length=200,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Logradouro",
    )
    nome_complemento = models.CharField(
        db_column="no_complemento",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Complemento",
    )
    nome_bairro = models.CharField(
        db_column="no_bairro",
        max_length=40,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Bairro",
    )
    numero_endereco = models.CharField(
        db_column="nr_endereco",
        max_length=10,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Número do Endereço",
    )
    numero_cep = models.CharField(
        db_column="nr_cep",
        max_length=8,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="CEP",
    )
    cd_pais = models.CharField(
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="País",
    )
    sg_uf = models.CharField(
        max_length=2,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="UF",
    )
    id_municipio = models.ForeignKey(
        Municipio,
        models.DO_NOTHING,
        db_column="id_municipio",
        blank=True,
        null=True,
        verbose_name="Município",
    )
    numero_telefone_nf = models.CharField(
        db_column="nr_telefone_nf",
        max_length=11,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Telefone NF",
    )
    numero_telefone = models.CharField(
        db_column="nr_telefone",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Telefone",
    )
    st_empresa = models.CharField(
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Status da Empresa",
    )
    nome_email_administrativo = models.CharField(
        db_column="no_email_administrativo",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail Administrativo",
    )
    nome_email_geral = models.CharField(
        db_column="no_email_geral",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail Geral",
    )
    nome_email_from = models.CharField(
        db_column="no_email_from",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail de Origem",
    )
    nome_email_replyto = models.CharField(
        db_column="no_email_replyto",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail de Resposta",
    )
    nome_dominio_smi = models.CharField(
        db_column="no_dominio_smi",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Domínio SMI",
    )
    nome_dominio_cliente = models.CharField(
        db_column="no_dominio_cliente",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Domínio do Cliente",
    )
    nome_email_proposta = models.CharField(
        db_column="no_email_proposta",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail para Propostas",
    )
    path_personalizacao = models.CharField(
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Caminho de Personalização",
    )
    cd_cnae = models.CharField(
        max_length=7,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="CNAE",
    )
    info_complementar = models.CharField(
        db_column="tt_info_complementar",
        max_length=500,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Informações Complementares",
    )
    numero_serie_atual_nf = models.CharField(
        db_column="nr_serie_atual_nf",
        max_length=3,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Número de Série Atual (NF)",
    )
    tipo_ambiente_nf = models.CharField(
        db_column="tp_ambiente_nf",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Tipo de Ambiente (NF)",
    )
    descricao_natureza_operacao = models.CharField(
        db_column="ds_natureza_operacao",
        max_length=50,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Natureza da Operação",
    )
    valor_aliquota_issqn = models.DecimalField(
        db_column="vl_aliquota_issqn",
        max_digits=10,
        decimal_places=4,
        blank=True,
        null=True,
        verbose_name="Alíquota ISSQN",
    )
    cd_servico_issqn = models.CharField(
        max_length=5,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Serviço ISSQN",
    )
    cd_regime_tributacao = models.CharField(
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Regime de Tributação",
    )
    numero_insc_municipal = models.CharField(
        db_column="nr_insc_municipal",
        max_length=13,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Inscrição Municipal",
    )
    tipo_servico_nf = models.CharField(
        db_column="tp_servico_nf",
        max_length=6,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Tipo de Serviço (NF)",
    )
    cd_regime_tributario = models.CharField(
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Regime Tributário",
    )
    nome_email_contador = models.CharField(
        db_column="no_email_contador",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail do Contador",
    )
    in_smi_gerar_servico_contrato = models.CharField(
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Geração de Serviço Contrato (SMI)",
    )
    in_force_https = models.CharField(
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Forçar HTTPS",
    )

    class Meta:
        managed = False
        db_table = "erp_empresa"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome_empresa
