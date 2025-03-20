from django.db import models
from empresas.models import ErpEmpresa
from veiculos.models import Municipio, Uf


class ErpCliente(models.Model):
    id_cliente = models.AutoField(primary_key=True, verbose_name="ID do Cliente")
    numero_cnpj = models.CharField(
        db_column="nr_cnpj",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="CNPJ",
    )
    numero_cpf = models.CharField(
        db_column="nr_cpf",
        max_length=11,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="CPF",
    )
    nome_cliente = models.CharField(
        db_column="no_cliente",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Nome do Cliente",
    )
    nome_razao_social = models.CharField(
        db_column="no_razao_social",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Razão Social",
    )
    numero_inscricao_estadual = models.CharField(
        db_column="nr_insc_estadual",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Inscrição Estadual",
    )
    endereco = models.CharField(
        db_column="no_endereco",
        max_length=600,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Endereço",
    )
    telefone_gestor = models.CharField(
        db_column="nr_telefone_gestor",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Telefone do Gestor",
    )
    email_gestor = models.CharField(
        db_column="no_email_gestor",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail do Gestor",
    )
    contato_gestor = models.CharField(
        db_column="no_contato_gestor",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Contato do Gestor",
    )
    contato_financeiro = models.CharField(
        db_column="no_contato_financeiro",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Contato Financeiro",
    )
    telefone_financeiro = models.CharField(
        db_column="nr_telefone_financeiro",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Telefone Financeiro",
    )
    email_financeiro = models.CharField(
        db_column="no_email_financeiro",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail Financeiro",
    )
    contato_usuario = models.CharField(
        db_column="no_contato_usuario",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Contato do Usuário",
    )
    telefone_usuario = models.CharField(
        db_column="nr_telefone_usuario",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Telefone do Usuário",
    )
    email_usuario = models.CharField(
        db_column="no_email_usuario",
        max_length=80,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="E-mail do Usuário",
    )
    status_cliente = models.CharField(
        db_column="st_cliente",
        max_length=1,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        verbose_name="Status do Cliente",
    )
    data_cadastro = models.DateTimeField(
        db_column="dt_cadastro", verbose_name="Data de Cadastro"
    )
    numero_inscricao_municipal = models.CharField(
        db_column="nr_insc_municipal",
        max_length=14,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Inscrição Municipal",
    )
    logradouro = models.CharField(
        db_column="no_logradouro",
        max_length=200,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Logradouro",
    )
    complemento = models.CharField(
        db_column="no_complemento",
        max_length=100,
        db_collation="SQL_Latin1_General_CP1_CI_AS",
        blank=True,
        null=True,
        verbose_name="Complemento",
    )
    bairro = models.CharField(
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
        verbose_name="Número",
    )
    cep = models.CharField(
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
        verbose_name="Código do País",
    )
    cd_uf = models.ForeignKey(
        Uf,
        on_delete=models.DO_NOTHING,
        db_column="sg_uf",
        max_length=2,  # FK
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
    id_ultimo_servico_pago = models.IntegerField(
        blank=True, null=True, verbose_name="ID do Último Serviço Pago"
    )
    sigla_cliente = models.CharField(
        db_column="sigla_cliente",
        max_length=10,
        blank=True,
        null=True,
        verbose_name="Sigla do Cliente",
    )

    class Meta:
        managed = False
        db_table = "erp_cliente"
        verbose_name = "ERP Cliente"
        verbose_name_plural = "ERP Clientes"
        ordering = ["id_cliente"]

    def __str__(self):
        return self.nome_cliente
