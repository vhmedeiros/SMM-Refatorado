USE [bdNewsUp]
GO
/****** Object:  Table [dbo].[auth_group]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](150) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_group_name_a6ea08ec_uniq] UNIQUE NONCLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_group_permissions]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group_permissions](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[group_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_permission]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_permission](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[content_type_id] [int] NOT NULL,
	[codename] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_user]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_user](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[password] [nvarchar](128) NOT NULL,
	[last_login] [datetimeoffset](7) NULL,
	[is_superuser] [bit] NOT NULL,
	[username] [nvarchar](150) NOT NULL,
	[first_name] [nvarchar](150) NOT NULL,
	[last_name] [nvarchar](150) NOT NULL,
	[email] [nvarchar](254) NOT NULL,
	[is_staff] [bit] NOT NULL,
	[is_active] [bit] NOT NULL,
	[date_joined] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_user_username_6821ab7c_uniq] UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_user_groups]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_user_groups](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NOT NULL,
	[group_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_user_user_permissions]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_user_user_permissions](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[CategoriaPalavraChave]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[CategoriaPalavraChave](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome] [nvarchar](510) NULL,
	[id_cliente] [int] NULL,
	[status] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [UQ__Categori__6F71C0DC7D6DF8DD] UNIQUE NONCLUSTERED 
(
	[nome] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[configuracao_cliente]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[configuracao_cliente](
	[id_configuracao] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[nome_cliente_sistema] [nvarchar](510) NOT NULL,
	[id_empresa_prestadora] [char](3) NOT NULL,
	[logotipo] [nvarchar](510) NULL,
	[cor_primaria] [nvarchar](14) NOT NULL,
	[cor_secundaria] [nvarchar](14) NOT NULL,
	[sigla_cliente] [varchar](10) NOT NULL,
	[url_pagina_cliente] [varchar](255) NULL,
	[status_pagina] [char](1) NOT NULL,
	[data_ativacao] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_configuracao] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[id_cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[contato_cliente]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[contato_cliente](
	[id_contato] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[nome] [nvarchar](255) NOT NULL,
	[email] [nvarchar](255) NOT NULL,
	[telefone] [nvarchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_contato] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_admin_log]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_admin_log](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[action_time] [datetimeoffset](7) NOT NULL,
	[object_id] [nvarchar](max) NULL,
	[object_repr] [nvarchar](200) NOT NULL,
	[action_flag] [smallint] NOT NULL,
	[change_message] [nvarchar](max) NOT NULL,
	[content_type_id] [int] NULL,
	[user_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_content_type]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_content_type](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app_label] [nvarchar](100) NOT NULL,
	[model] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_migrations]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_migrations](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[app] [nvarchar](255) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[applied] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_session]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_session](
	[session_key] [nvarchar](40) NOT NULL,
	[session_data] [nvarchar](max) NOT NULL,
	[expire_date] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[session_key] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[envio_email]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[envio_email](
	[id_envio] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[nome_disparo] [nvarchar](255) NOT NULL,
	[data_agendamento] [datetime] NOT NULL,
	[categorias] [nvarchar](max) NOT NULL,
	[veiculos] [nvarchar](max) NOT NULL,
	[status] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_envio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_cliente]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_cliente](
	[id_cliente] [int] IDENTITY(4,1) NOT NULL,
	[nr_cnpj] [char](14) NULL,
	[nr_cpf] [char](11) NULL,
	[no_cliente] [varchar](100) NOT NULL,
	[no_razao_social] [varchar](100) NULL,
	[nr_insc_estadual] [char](14) NULL,
	[no_endereco] [varchar](600) NULL,
	[nr_telefone_gestor] [char](14) NULL,
	[no_email_gestor] [varchar](80) NULL,
	[no_contato_gestor] [varchar](80) NULL,
	[no_contato_financeiro] [varchar](80) NULL,
	[nr_telefone_financeiro] [char](14) NULL,
	[no_email_financeiro] [varchar](80) NULL,
	[no_contato_usuario] [varchar](80) NULL,
	[nr_telefone_usuario] [char](14) NULL,
	[no_email_usuario] [varchar](80) NULL,
	[st_cliente] [char](1) NOT NULL,
	[dt_cadastro] [datetime] NOT NULL,
	[nr_insc_municipal] [char](14) NULL,
	[no_logradouro] [varchar](200) NULL,
	[no_complemento] [varchar](100) NULL,
	[no_bairro] [varchar](40) NULL,
	[nr_endereco] [char](10) NULL,
	[nr_cep] [char](8) NULL,
	[cd_pais] [char](3) NULL,
	[sg_uf] [char](2) NULL,
	[id_municipio] [int] NULL,
	[id_ultimo_servico_pago] [int] NULL,
	[sigla_cliente] [nvarchar](20) NULL,
	[modificado_por] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_cliente] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_cliente_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_cliente_contato](
	[id_cliente] [int] NOT NULL,
	[id_contato] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_cliente_old]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_cliente_old](
	[id_cliente] [smallint] NULL,
	[nr_cnpj] [bigint] NULL,
	[nr_cpf] [nvarchar](50) NULL,
	[no_cliente] [nvarchar](100) NULL,
	[no_razao_social] [nvarchar](100) NULL,
	[nr_insc_estadual] [nvarchar](50) NULL,
	[no_endereco] [nvarchar](300) NULL,
	[nr_telefone_gestor] [nvarchar](50) NULL,
	[no_email_gestor] [nvarchar](100) NULL,
	[no_contato_gestor] [nvarchar](100) NULL,
	[no_contato_financeiro] [nvarchar](100) NULL,
	[nr_telefone_financeiro] [nvarchar](50) NULL,
	[no_email_financeiro] [nvarchar](50) NULL,
	[no_contato_usuario] [nvarchar](100) NULL,
	[nr_telefone_usuario] [nvarchar](50) NULL,
	[no_email_usuario] [nvarchar](50) NULL,
	[st_cliente] [nvarchar](50) NULL,
	[dt_cadastro] [datetime2](7) NULL,
	[nr_insc_municipal] [nvarchar](50) NULL,
	[no_logradouro] [nvarchar](250) NULL,
	[no_complemento] [nvarchar](100) NULL,
	[no_bairro] [nvarchar](50) NULL,
	[nr_endereco] [nvarchar](50) NULL,
	[nr_cep] [int] NULL,
	[cd_pais] [nvarchar](50) NULL,
	[sg_uf] [nvarchar](50) NULL,
	[id_municipio] [smallint] NULL,
	[id_ultimo_servico_pago] [nvarchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_contato](
	[id_contato] [int] NOT NULL,
	[no_contato] [char](50) NOT NULL,
	[st_contato] [char](1) NOT NULL,
	[no_departamento] [varchar](100) NULL,
	[no_cargo] [varchar](50) NULL,
	[no_endereco] [varchar](1000) NULL,
	[nr_telefone_trabalho] [char](15) NULL,
	[nr_telefone_celular] [char](15) NULL,
	[nr_telefone_particular] [char](15) NULL,
	[no_email_trabalho] [varchar](100) NULL,
	[no_email_particular] [varchar](100) NULL,
	[tt_observacao] [varchar](1000) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_contrato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_contrato](
	[id_contrato] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[cd_empresa] [char](3) NOT NULL,
	[cd_identificacao] [char](20) NULL,
	[descricao_contrato] [varchar](1000) NOT NULL,
	[data_inicio_vigencia] [date] NOT NULL,
	[data_fim_vigencia] [date] NOT NULL,
	[tipo_prorrogacao] [char](3) NOT NULL,
	[descricao_objeto] [varchar](max) NOT NULL,
	[informacao_adicional] [varchar](max) NULL,
	[valor_contrato] [money] NOT NULL,
	[dia_emissao_nota_fiscal] [int] NOT NULL,
	[status_contrato] [char](1) NOT NULL,
	[in_contrato_assinado] [bit] NOT NULL,
	[tipo_cobranca] [char](3) NOT NULL,
	[data_cadastro] [datetime] NOT NULL,
	[dia_do_pagamento] [int] NOT NULL,
	[dia_aviso_fim_vigencia] [int] NULL,
	[forma_envio_nf] [char](1) NULL,
	[modificado_por] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_contrato] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_contrato_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_contrato_contato](
	[id_contrato] [int] NOT NULL,
	[id_contato] [int] NOT NULL,
	[tp_contato] [char](1) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_empresa]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_empresa](
	[cd_empresa] [char](3) NOT NULL,
	[nr_cnpj] [char](14) NOT NULL,
	[no_empresa] [varchar](100) NOT NULL,
	[no_razao_social] [varchar](300) NOT NULL,
	[no_fantasia] [varchar](300) NULL,
	[nr_insc_estadual] [char](13) NULL,
	[nr_reg_contab] [char](5) NULL,
	[no_endereco] [varchar](1000) NULL,
	[no_logradouro] [varchar](200) NULL,
	[no_complemento] [varchar](100) NULL,
	[no_bairro] [varchar](40) NULL,
	[nr_endereco] [char](10) NULL,
	[nr_cep] [char](8) NULL,
	[cd_pais] [char](3) NULL,
	[sg_uf] [char](2) NULL,
	[id_municipio] [int] NULL,
	[nr_telefone_nf] [varchar](11) NULL,
	[nr_telefone] [varchar](50) NULL,
	[st_empresa] [char](1) NOT NULL,
	[no_email_administrativo] [varchar](500) NULL,
	[no_email_geral] [varchar](500) NULL,
	[no_email_from] [varchar](100) NULL,
	[no_email_replyto] [varchar](100) NULL,
	[no_dominio_smi] [varchar](100) NULL,
	[no_dominio_cliente] [varchar](100) NULL,
	[no_email_proposta] [varchar](500) NULL,
	[path_personalizacao] [varchar](50) NULL,
	[cd_cnae] [char](7) NULL,
	[tt_info_complementar] [varchar](500) NULL,
	[nr_serie_atual_nf] [char](3) NULL,
	[tp_ambiente_nf] [char](1) NULL,
	[ds_natureza_operacao] [varchar](50) NULL,
	[vl_aliquota_issqn] [decimal](10, 4) NULL,
	[cd_servico_issqn] [char](5) NULL,
	[cd_regime_tributacao] [char](1) NULL,
	[nr_insc_municipal] [char](13) NULL,
	[tp_servico_nf] [char](6) NULL,
	[cd_regime_tributario] [char](1) NULL,
	[no_email_contador] [varchar](100) NULL,
	[in_smi_gerar_servico_contrato] [char](1) NOT NULL,
	[in_force_https] [char](1) NULL,
	[modificado_por] [int] NULL,
 CONSTRAINT [PK_erp_empresa] PRIMARY KEY CLUSTERED 
(
	[cd_empresa] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_equipamento]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_equipamento](
	[id_equipamento] [int] NOT NULL,
	[cd_empresa_proprietaria] [char](3) NOT NULL,
	[ds_equipamento] [varchar](500) NULL,
	[tp_equipamento] [varchar](200) NOT NULL,
	[st_equipamento] [char](1) NOT NULL,
	[num_canais] [int] NULL,
	[no_endereco] [varchar](1000) NULL,
	[nr_latitude] [varchar](20) NULL,
	[cd_pais] [char](3) NOT NULL,
	[sg_uf] [char](2) NOT NULL,
	[id_municipio] [int] NOT NULL,
	[vl_equipamento] [money] NULL,
	[nr_longitude] [varchar](20) NULL,
	[cd_empresa_beneficiada] [char](3) NOT NULL,
	[login_eq] [varchar](50) NULL,
	[senha] [varchar](50) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_equipamento_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_equipamento_contato](
	[id_equipamento] [int] NOT NULL,
	[id_contato] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_equipamento_responsavel]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_equipamento_responsavel](
	[id_equipamento] [int] NOT NULL,
	[id_funcionario] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_fornecedor_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_fornecedor_contato](
	[id_fornecedor] [int] NOT NULL,
	[id_contato] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_funcionario_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_funcionario_contato](
	[id_funcionario] [int] NOT NULL,
	[id_contato] [int] NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_produto]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_produto](
	[cd_produto] [int] IDENTITY(1,1) NOT NULL,
	[descricao] [nvarchar](100) NOT NULL,
	[situacao_produto] [bit] NOT NULL,
	[cd_produto_principal] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[cd_produto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_produto_veiculos]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_produto_veiculos](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[erpproduto_id] [int] NOT NULL,
	[veiculosistemas_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[erp_servico_contato]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[erp_servico_contato](
	[id_servico] [int] NOT NULL,
	[id_contato] [int] NOT NULL,
	[tp_contato] [char](1) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Evento]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Evento](
	[id_evento] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[descricao] [nvarchar](255) NOT NULL,
	[data_hora] [datetime] NULL,
	[id_usuario] [int] NULL,
	[content_type_id] [int] NOT NULL,
	[object_id] [int] NOT NULL,
	[acao] [nvarchar](20) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id_evento] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[InstallSistemas]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[InstallSistemas](
	[CodSys] [int] NOT NULL,
	[no_cliente] [char](100) NULL,
	[NmoSys] [varchar](100) NOT NULL,
	[ativosys] [bit] NOT NULL,
	[diretoriosys] [varchar](25) NOT NULL,
	[cd_modelo] [char](4) NULL,
	[cd_ordenacao] [char](10) NULL,
	[tp_arquivo_preferencial] [char](3) NULL,
	[no_imagem_logo] [varchar](30) NULL,
	[cd_senha] [char](20) NULL,
	[in_bloqueio_site] [char](1) NULL,
	[in_avalia_noticia] [char](1) NULL,
	[PalavrasSys] [varchar](500) NULL,
	[no_grupo_veiculo_ordenado] [char](40) NULL,
	[no_grupo_veiculo_nao_ordenado] [char](40) NULL,
	[no_grupo_veiculo_coluna] [char](40) NULL,
	[in_email_bloqueado] [char](1) NULL,
	[id_google_analytics] [char](20) NULL,
	[tt_observacao] [varchar](2000) NULL,
	[in_site_iis_ok] [char](1) NULL,
	[in_materia_dia_publicacao] [char](1) NULL,
	[in_apenas_veiculo_contratado] [char](1) NULL,
	[id_cliente] [int] NULL,
	[tp_sistema] [char](3) NULL,
	[in_apenas_categoria_principal] [char](1) NULL,
	[id_contrato] [int] NULL,
	[id_proposta] [int] NULL,
	[in_exibe_espaco_ocupado] [char](1) NULL,
	[in_exibe_valoracao] [char](1) NULL,
	[in_exibe_avaliacao] [char](1) NULL,
	[cd_empresa] [char](3) NOT NULL,
	[dt_ativacao] [datetime] NULL,
	[in_obrigatorio_usuario_senha] [char](1) NULL,
	[in_exibe_logo_noticia] [char](1) NULL,
	[In_incluir_vinheta] [char](1) NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[lingua]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[lingua](
	[cd_lingua] [char](2) NOT NULL,
	[no_lingua] [nvarchar](50) NULL,
 CONSTRAINT [PK_lingua] PRIMARY KEY CLUSTERED 
(
	[cd_lingua] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[municipio]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[municipio](
	[id_municipio] [int] NOT NULL,
	[id_mesorregiao] [tinyint] NOT NULL,
	[uf_municipio] [char](2) NOT NULL,
	[no_municipio] [nvarchar](100) NULL,
	[nr_latitude] [float] NULL,
	[nr_longitude] [float] NULL,
	[id_municipio_ibge] [int] NULL,
 CONSTRAINT [PK_municipio] PRIMARY KEY CLUSTERED 
(
	[id_municipio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[noticia_importada]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[noticia_importada](
	[cd_noticia] [int] IDENTITY(1,1) NOT NULL,
	[id_importacao] [int] NULL,
	[dt_importacao] [datetime] NOT NULL,
	[dt_noticia] [smalldatetime] NOT NULL,
	[no_titulo] [nvarchar](500) NULL,
	[tt_noticia] [nvarchar](4000) NULL,
	[id_veiculo] [int] NOT NULL,
	[ds_url] [varchar](500) NOT NULL,
	[tt_sutia] [varchar](1000) NULL,
	[id_editoria] [int] NULL,
	[no_colunista] [nvarchar](1000) NULL,
	[ds_url_media] [varchar](2000) NULL,
	[cd_pagina] [char](6) NULL,
	[clientes_relacionados] [nvarchar](max) NULL,
	[categorias_relacionadas] [nvarchar](max) NULL,
	[processado] [bit] NULL,
	[imagem] [nvarchar](255) NULL,
	[modificado_por] [int] NULL,
 CONSTRAINT [PK_noticia_importada] PRIMARY KEY CLUSTERED 
(
	[cd_noticia] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[noticia_importada_backup]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[noticia_importada_backup](
	[cd_noticia] [int] IDENTITY(1,1) NOT NULL,
	[id_importacao] [int] NULL,
	[dt_importacao] [datetime] NOT NULL,
	[dt_noticia] [smalldatetime] NOT NULL,
	[no_titulo] [varchar](500) NOT NULL,
	[tt_noticia] [varchar](max) NOT NULL,
	[id_veiculo] [int] NOT NULL,
	[ds_url] [varchar](500) NOT NULL,
	[tt_sutia] [varchar](1000) NULL,
	[id_editoria] [int] NULL,
	[no_colunista] [varchar](1000) NULL,
	[ds_url_media] [varchar](2000) NULL,
	[cd_pagina] [char](6) NULL,
	[clientes_relacionados] [nvarchar](max) NULL,
	[categorias_relacionadas] [nvarchar](max) NULL,
	[processado] [bit] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[pais]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[pais](
	[cd_pais] [nvarchar](6) NOT NULL,
	[no_pais] [nvarchar](200) NULL,
	[cd_pais_ibge] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_pais] PRIMARY KEY CLUSTERED 
(
	[cd_pais] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[PalavraChave]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[PalavraChave](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[id_categoria] [int] NOT NULL,
	[palavra] [nvarchar](510) NULL,
	[data_cadastro] [datetime] NULL,
	[status] [bit] NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sites_cliente]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sites_cliente](
	[id_site] [int] IDENTITY(1,1) NOT NULL,
	[id_cliente] [int] NOT NULL,
	[nome_site] [nvarchar](255) NOT NULL,
	[dominio] [nvarchar](255) NOT NULL,
	[cor_primaria] [nvarchar](7) NOT NULL,
	[cor_secundaria] [nvarchar](7) NOT NULL,
	[logotipo] [nvarchar](255) NULL,
	[data_criacao] [datetime] NULL,
PRIMARY KEY CLUSTERED 
(
	[id_site] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[dominio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[smc_gravador_computador]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[smc_gravador_computador](
	[fk_id_computador] [int] NOT NULL,
	[fk_cd_gravador] [char](5) NOT NULL,
	[id_gravador_computador] [int] IDENTITY(1,1) NOT NULL,
	[fk_id_equipamento] [int] NULL,
 CONSTRAINT [PK_smi_tipo_maquina] PRIMARY KEY CLUSTERED 
(
	[id_gravador_computador] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[smi_computador]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[smi_computador](
	[id_computador] [int] IDENTITY(1,1) NOT NULL,
	[cd_computador_md5] [varchar](35) NOT NULL,
	[informacoes_computador] [varchar](max) NULL,
	[st_smc_computador] [char](1) NOT NULL,
	[fk_id_equipamento] [int] NULL,
	[cd_computador] [varchar](35) NULL,
	[tp_ip_publico] [char](1) NULL,
	[nr_ip_local] [varchar](50) NULL,
	[nr_porta] [varchar](6) NULL,
	[nr_ip_publico] [varchar](50) NULL,
	[nr_porta_publico] [varchar](6) NULL,
 CONSTRAINT [PK_smi_maquina] PRIMARY KEY CLUSTERED 
(
	[id_computador] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[tipo_veiculo]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[tipo_veiculo](
	[tp_veiculo] [char](3) NOT NULL,
	[ds_tipo_veiculo] [nvarchar](50) NOT NULL,
 CONSTRAINT [PK_tipo_veiculo] PRIMARY KEY CLUSTERED 
(
	[tp_veiculo] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[uf]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[uf](
	[sg_uf] [char](2) NOT NULL,
	[no_uf] [nvarchar](100) NULL,
	[no_regiao] [nvarchar](50) NOT NULL,
	[cd_uf_ibge] [tinyint] NULL,
	[cd_pais] [nvarchar](50) NULL,
	[id_capital] [smallint] NULL,
	[nr_gmt] [nvarchar](50) NULL,
 CONSTRAINT [PK_uf] PRIMARY KEY CLUSTERED 
(
	[sg_uf] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[VeiculoSistemas]    Script Date: 26/03/2025 09:54:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[VeiculoSistemas](
	[CodVei] [int] IDENTITY(1,1) NOT NULL,
	[CodSys] [int] NULL,
	[NmoVei] [nvarchar](1020) NULL,
	[PriVei] [nvarchar](2) NULL,
	[VeiNacional] [bit] NULL,
	[VeiOrdem] [int] NULL,
	[CodTipoVei] [int] NULL,
	[sg_uf] [char](2) NULL,
	[tp_veiculo] [char](3) NOT NULL,
	[st_veiculo] [char](1) NULL,
	[end_veiculo] [varchar](500) NULL,
	[no_identificador_url] [varchar](100) NULL,
	[dt_ultima_noticia] [datetime] NULL,
	[cd_usuario_web] [char](60) NULL,
	[cd_senha_web] [char](60) NULL,
	[cd_pais] [nvarchar](6) NOT NULL,
	[cd_lingua] [char](2) NULL,
	[vl_publicitario_cm] [money] NULL,
	[cd_usuario_flip] [char](60) NULL,
	[cd_senha_flip] [char](60) NULL,
	[no_referencia] [varchar](500) NULL,
	[end_flip] [varchar](500) NULL,
	[id_municipio] [int] NULL,
	[no_url_stream] [varchar](4000) NULL,
	[in_domingo] [char](1) NULL,
	[in_segunda] [char](1) NULL,
	[in_terca] [char](1) NULL,
	[in_quarta] [char](1) NULL,
	[in_quinta] [char](1) NULL,
	[in_sexta] [char](1) NULL,
	[in_sabado] [char](1) NULL,
	[st_url_stream] [char](3) NULL,
	[qt_publico] [int] NULL,
	[nr_telefone] [varchar](30) NULL,
	[no_endereco] [varchar](300) NULL,
	[dt_atualizacao] [date] NULL,
	[tolerancia_sem_noticia] [int] NULL,
	[qt_min_noticia] [int] NULL,
	[periodo_publicacao] [char](1) NULL,
	[tt_comando_encoder] [varchar](2000) NULL,
	[cm_altura] [decimal](6, 2) NULL,
	[cm_largura] [decimal](6, 2) NULL,
	[json_lst_etiqueta] [varchar](max) NULL,
	[in_extrair_texto_ocr] [char](1) NULL,
	[modificado_por] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[CodVei] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[CategoriaPalavraChave] ADD  DEFAULT ((1)) FOR [status]
GO
ALTER TABLE [dbo].[configuracao_cliente] ADD  DEFAULT ('#000000') FOR [cor_primaria]
GO
ALTER TABLE [dbo].[configuracao_cliente] ADD  DEFAULT ('#FFFFFF') FOR [cor_secundaria]
GO
ALTER TABLE [dbo].[configuracao_cliente] ADD  DEFAULT ('I') FOR [status_pagina]
GO
ALTER TABLE [dbo].[envio_email] ADD  DEFAULT ('Pendente') FOR [status]
GO
ALTER TABLE [dbo].[Evento] ADD  DEFAULT (getdate()) FOR [data_hora]
GO
ALTER TABLE [dbo].[noticia_importada] ADD  DEFAULT ((0)) FOR [processado]
GO
ALTER TABLE [dbo].[PalavraChave] ADD  DEFAULT (getdate()) FOR [data_cadastro]
GO
ALTER TABLE [dbo].[PalavraChave] ADD  DEFAULT ((1)) FOR [status]
GO
ALTER TABLE [dbo].[sites_cliente] ADD  DEFAULT ('#000000') FOR [cor_primaria]
GO
ALTER TABLE [dbo].[sites_cliente] ADD  DEFAULT ('#FFFFFF') FOR [cor_secundaria]
GO
ALTER TABLE [dbo].[sites_cliente] ADD  DEFAULT (getdate()) FOR [data_criacao]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[auth_permission]  WITH CHECK ADD  CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[auth_permission] CHECK CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[auth_user_groups]  WITH CHECK ADD  CONSTRAINT [auth_user_groups_group_id_97559544_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[auth_user_groups] CHECK CONSTRAINT [auth_user_groups_group_id_97559544_fk_auth_group_id]
GO
ALTER TABLE [dbo].[auth_user_groups]  WITH CHECK ADD  CONSTRAINT [auth_user_groups_user_id_6a12ed8b_fk_auth_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[auth_user_groups] CHECK CONSTRAINT [auth_user_groups_user_id_6a12ed8b_fk_auth_user_id]
GO
ALTER TABLE [dbo].[auth_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [auth_user_user_permissions_permission_id_1fbb5f2c_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[auth_user_user_permissions] CHECK CONSTRAINT [auth_user_user_permissions_permission_id_1fbb5f2c_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[auth_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[auth_user_user_permissions] CHECK CONSTRAINT [auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id]
GO
ALTER TABLE [dbo].[CategoriaPalavraChave]  WITH CHECK ADD  CONSTRAINT [fk_categoria_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[CategoriaPalavraChave] CHECK CONSTRAINT [fk_categoria_cliente]
GO
ALTER TABLE [dbo].[configuracao_cliente]  WITH CHECK ADD  CONSTRAINT [fk_configuracao_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[configuracao_cliente] CHECK CONSTRAINT [fk_configuracao_cliente]
GO
ALTER TABLE [dbo].[configuracao_cliente]  WITH CHECK ADD  CONSTRAINT [fk_configuracao_empresa] FOREIGN KEY([id_empresa_prestadora])
REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO
ALTER TABLE [dbo].[configuracao_cliente] CHECK CONSTRAINT [fk_configuracao_empresa]
GO
ALTER TABLE [dbo].[contato_cliente]  WITH CHECK ADD  CONSTRAINT [fk_contato_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[contato_cliente] CHECK CONSTRAINT [fk_contato_cliente]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_user_id_c564eba6_fk_auth_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_user_id_c564eba6_fk_auth_user_id]
GO
ALTER TABLE [dbo].[envio_email]  WITH CHECK ADD  CONSTRAINT [fk_envio_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[envio_email] CHECK CONSTRAINT [fk_envio_cliente]
GO
ALTER TABLE [dbo].[erp_cliente]  WITH CHECK ADD  CONSTRAINT [FK_erp_cliente_modificado] FOREIGN KEY([modificado_por])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[erp_cliente] CHECK CONSTRAINT [FK_erp_cliente_modificado]
GO
ALTER TABLE [dbo].[erp_cliente]  WITH CHECK ADD  CONSTRAINT [FK_erp_cliente_municipio] FOREIGN KEY([id_municipio])
REFERENCES [dbo].[municipio] ([id_municipio])
GO
ALTER TABLE [dbo].[erp_cliente] CHECK CONSTRAINT [FK_erp_cliente_municipio]
GO
ALTER TABLE [dbo].[erp_cliente]  WITH CHECK ADD  CONSTRAINT [FK_erp_cliente_uf] FOREIGN KEY([sg_uf])
REFERENCES [dbo].[uf] ([sg_uf])
GO
ALTER TABLE [dbo].[erp_cliente] CHECK CONSTRAINT [FK_erp_cliente_uf]
GO
ALTER TABLE [dbo].[erp_contrato]  WITH CHECK ADD  CONSTRAINT [FK_erp_contrato_erp_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[erp_contrato] CHECK CONSTRAINT [FK_erp_contrato_erp_cliente]
GO
ALTER TABLE [dbo].[erp_contrato]  WITH CHECK ADD  CONSTRAINT [FK_erp_contrato_erp_empresa] FOREIGN KEY([cd_empresa])
REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO
ALTER TABLE [dbo].[erp_contrato] CHECK CONSTRAINT [FK_erp_contrato_erp_empresa]
GO
ALTER TABLE [dbo].[erp_contrato]  WITH CHECK ADD  CONSTRAINT [FK_erp_contrato_modificado] FOREIGN KEY([modificado_por])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[erp_contrato] CHECK CONSTRAINT [FK_erp_contrato_modificado]
GO
ALTER TABLE [dbo].[erp_empresa]  WITH CHECK ADD  CONSTRAINT [FK_erp_empresa_modificado] FOREIGN KEY([modificado_por])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[erp_empresa] CHECK CONSTRAINT [FK_erp_empresa_modificado]
GO
ALTER TABLE [dbo].[erp_empresa]  WITH CHECK ADD  CONSTRAINT [FK_erp_empresa_municipio] FOREIGN KEY([id_municipio])
REFERENCES [dbo].[municipio] ([id_municipio])
GO
ALTER TABLE [dbo].[erp_empresa] CHECK CONSTRAINT [FK_erp_empresa_municipio]
GO
ALTER TABLE [dbo].[erp_produto]  WITH CHECK ADD  CONSTRAINT [erp_produto_cd_produto_principal_ed8fcb7c_fk_erp_produto_cd_produto] FOREIGN KEY([cd_produto_principal])
REFERENCES [dbo].[erp_produto] ([cd_produto])
GO
ALTER TABLE [dbo].[erp_produto] CHECK CONSTRAINT [erp_produto_cd_produto_principal_ed8fcb7c_fk_erp_produto_cd_produto]
GO
ALTER TABLE [dbo].[erp_produto_veiculos]  WITH CHECK ADD  CONSTRAINT [erp_produto_veiculos_erpproduto_id_b9ff0c14_fk_erp_produto_cd_produto] FOREIGN KEY([erpproduto_id])
REFERENCES [dbo].[erp_produto] ([cd_produto])
GO
ALTER TABLE [dbo].[erp_produto_veiculos] CHECK CONSTRAINT [erp_produto_veiculos_erpproduto_id_b9ff0c14_fk_erp_produto_cd_produto]
GO
ALTER TABLE [dbo].[erp_produto_veiculos]  WITH CHECK ADD  CONSTRAINT [erp_produto_veiculos_veiculosistemas_id_3ae7ab8d_fk_VeiculoSistemas_CodVei] FOREIGN KEY([veiculosistemas_id])
REFERENCES [dbo].[VeiculoSistemas] ([CodVei])
GO
ALTER TABLE [dbo].[erp_produto_veiculos] CHECK CONSTRAINT [erp_produto_veiculos_veiculosistemas_id_3ae7ab8d_fk_VeiculoSistemas_CodVei]
GO
ALTER TABLE [dbo].[Evento]  WITH CHECK ADD FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[Evento]  WITH CHECK ADD  CONSTRAINT [FK_evento_content_type] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[Evento] CHECK CONSTRAINT [FK_evento_content_type]
GO
ALTER TABLE [dbo].[Evento]  WITH CHECK ADD  CONSTRAINT [fk_evento_usuario] FOREIGN KEY([id_usuario])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[Evento] CHECK CONSTRAINT [fk_evento_usuario]
GO
ALTER TABLE [dbo].[InstallSistemas]  WITH CHECK ADD  CONSTRAINT [FK_InstallSistemas_erp_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[InstallSistemas] CHECK CONSTRAINT [FK_InstallSistemas_erp_cliente]
GO
ALTER TABLE [dbo].[InstallSistemas]  WITH CHECK ADD  CONSTRAINT [FK_InstallSistemas_erp_empresa] FOREIGN KEY([cd_empresa])
REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO
ALTER TABLE [dbo].[InstallSistemas] CHECK CONSTRAINT [FK_InstallSistemas_erp_empresa]
GO
ALTER TABLE [dbo].[municipio]  WITH CHECK ADD  CONSTRAINT [FK_municipio_uf] FOREIGN KEY([uf_municipio])
REFERENCES [dbo].[uf] ([sg_uf])
GO
ALTER TABLE [dbo].[municipio] CHECK CONSTRAINT [FK_municipio_uf]
GO
ALTER TABLE [dbo].[noticia_importada]  WITH CHECK ADD  CONSTRAINT [FK_noticia_importada_modificado] FOREIGN KEY([modificado_por])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[noticia_importada] CHECK CONSTRAINT [FK_noticia_importada_modificado]
GO
ALTER TABLE [dbo].[noticia_importada]  WITH CHECK ADD  CONSTRAINT [FK_noticia_importada_VeiculoSistemas] FOREIGN KEY([id_veiculo])
REFERENCES [dbo].[VeiculoSistemas] ([CodVei])
GO
ALTER TABLE [dbo].[noticia_importada] CHECK CONSTRAINT [FK_noticia_importada_VeiculoSistemas]
GO
ALTER TABLE [dbo].[PalavraChave]  WITH CHECK ADD FOREIGN KEY([id_categoria])
REFERENCES [dbo].[CategoriaPalavraChave] ([id])
GO
ALTER TABLE [dbo].[PalavraChave]  WITH CHECK ADD FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO
ALTER TABLE [dbo].[sites_cliente]  WITH CHECK ADD  CONSTRAINT [fk_site_cliente] FOREIGN KEY([id_cliente])
REFERENCES [dbo].[erp_cliente] ([id_cliente])
ON DELETE CASCADE
GO
ALTER TABLE [dbo].[sites_cliente] CHECK CONSTRAINT [fk_site_cliente]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_lingua] FOREIGN KEY([cd_lingua])
REFERENCES [dbo].[lingua] ([cd_lingua])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_lingua]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_modificado] FOREIGN KEY([modificado_por])
REFERENCES [dbo].[auth_user] ([id])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_modificado]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_Municipio] FOREIGN KEY([id_municipio])
REFERENCES [dbo].[municipio] ([id_municipio])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_Municipio]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_pais] FOREIGN KEY([cd_pais])
REFERENCES [dbo].[pais] ([cd_pais])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_pais]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_tipo_veiculo] FOREIGN KEY([tp_veiculo])
REFERENCES [dbo].[tipo_veiculo] ([tp_veiculo])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_tipo_veiculo]
GO
ALTER TABLE [dbo].[VeiculoSistemas]  WITH CHECK ADD  CONSTRAINT [FK_VeiculoSistemas_uf] FOREIGN KEY([sg_uf])
REFERENCES [dbo].[uf] ([sg_uf])
GO
ALTER TABLE [dbo].[VeiculoSistemas] CHECK CONSTRAINT [FK_VeiculoSistemas_uf]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_action_flag_a8637d59_check] CHECK  (([action_flag]>=(0)))
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_action_flag_a8637d59_check]
GO
