CREATE SCHEMA [dbo]
GO

CREATE TABLE [dbo].[smc_gravador_computador] (
  [fk_id_computador] int(10) NOT NULL,
  [fk_cd_gravador] char(5) NOT NULL,
  [id_gravador_computador] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [fk_id_equipamento] int(10)
)
GO

CREATE TABLE [dbo].[smi_computador] (
  [id_computador] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [cd_computador_md5] varchar(35) NOT NULL,
  [informacoes_computador] varchar(MAX),
  [st_smc_computador] char(1) NOT NULL,
  [fk_id_equipamento] int(10),
  [cd_computador] varchar(35),
  [tp_ip_publico] char(1),
  [nr_ip_local] varchar(50),
  [nr_porta] varchar(6),
  [nr_ip_publico] varchar(50),
  [nr_porta_publico] varchar(6)
)
GO

CREATE TABLE [dbo].[InstallSistemas] (
  [CodSys] int(10) NOT NULL,
  [no_cliente] char(100),
  [NmoSys] varchar(100) NOT NULL,
  [ativosys] bit NOT NULL,
  [diretoriosys] varchar(25) NOT NULL,
  [cd_modelo] char(4),
  [cd_ordenacao] char(10),
  [tp_arquivo_preferencial] char(3),
  [no_imagem_logo] varchar(30),
  [cd_senha] char(20),
  [in_bloqueio_site] char(1),
  [in_avalia_noticia] char(1),
  [PalavrasSys] varchar(500),
  [no_grupo_veiculo_ordenado] char(40),
  [no_grupo_veiculo_nao_ordenado] char(40),
  [no_grupo_veiculo_coluna] char(40),
  [in_email_bloqueado] char(1),
  [id_google_analytics] char(20),
  [tt_observacao] varchar(2000),
  [in_site_iis_ok] char(1),
  [in_materia_dia_publicacao] char(1),
  [in_apenas_veiculo_contratado] char(1),
  [id_cliente] int(10),
  [tp_sistema] char(3),
  [in_apenas_categoria_principal] char(1),
  [id_contrato] int(10),
  [id_proposta] int(10),
  [in_exibe_espaco_ocupado] char(1),
  [in_exibe_valoracao] char(1),
  [in_exibe_avaliacao] char(1),
  [cd_empresa] char(3) NOT NULL,
  [dt_ativacao] datetime,
  [in_obrigatorio_usuario_senha] char(1),
  [in_exibe_logo_noticia] char(1),
  [In_incluir_vinheta] char(1)
)
GO

CREATE TABLE [dbo].[erp_cliente_contato] (
  [id_cliente] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_contato] (
  [id_contato] int(10) NOT NULL,
  [no_contato] char(50) NOT NULL,
  [st_contato] char(1) NOT NULL,
  [no_departamento] varchar(100),
  [no_cargo] varchar(50),
  [no_endereco] varchar(1000),
  [nr_telefone_trabalho] char(15),
  [nr_telefone_celular] char(15),
  [nr_telefone_particular] char(15),
  [no_email_trabalho] varchar(100),
  [no_email_particular] varchar(100),
  [tt_observacao] varchar(1000)
)
GO

CREATE TABLE [dbo].[erp_contrato_contato] (
  [id_contrato] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL,
  [tp_contato] char(1) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_empresa] (
  [cd_empresa] char(3) PRIMARY KEY NOT NULL,
  [nr_cnpj] char(14) NOT NULL,
  [no_empresa] varchar(100) NOT NULL,
  [no_razao_social] varchar(300) NOT NULL,
  [no_fantasia] varchar(300),
  [nr_insc_estadual] char(13),
  [nr_reg_contab] char(5),
  [no_endereco] varchar(1000),
  [no_logradouro] varchar(200),
  [no_complemento] varchar(100),
  [no_bairro] varchar(40),
  [nr_endereco] char(10),
  [nr_cep] char(8),
  [cd_pais] char(3),
  [sg_uf] char(2),
  [id_municipio] int(10),
  [nr_telefone_nf] varchar(11),
  [nr_telefone] varchar(50),
  [st_empresa] char(1) NOT NULL,
  [no_email_administrativo] varchar(500),
  [no_email_geral] varchar(500),
  [no_email_from] varchar(100),
  [no_email_replyto] varchar(100),
  [no_dominio_smi] varchar(100),
  [no_dominio_cliente] varchar(100),
  [no_email_proposta] varchar(500),
  [path_personalizacao] varchar(50),
  [cd_cnae] char(7),
  [tt_info_complementar] varchar(500),
  [nr_serie_atual_nf] char(3),
  [tp_ambiente_nf] char(1),
  [ds_natureza_operacao] varchar(50),
  [vl_aliquota_issqn] decimal(10,4),
  [cd_servico_issqn] char(5),
  [cd_regime_tributacao] char(1),
  [nr_insc_municipal] char(13),
  [tp_servico_nf] char(6),
  [cd_regime_tributario] char(1),
  [no_email_contador] varchar(100),
  [in_smi_gerar_servico_contrato] char(1) NOT NULL,
  [in_force_https] char(1),
  [modificado_por] int(10)
)
GO

CREATE TABLE [dbo].[erp_equipamento] (
  [id_equipamento] int(10) NOT NULL,
  [cd_empresa_proprietaria] char(3) NOT NULL,
  [ds_equipamento] varchar(500),
  [tp_equipamento] varchar(200) NOT NULL,
  [st_equipamento] char(1) NOT NULL,
  [num_canais] int(10),
  [no_endereco] varchar(1000),
  [nr_latitude] varchar(20),
  [cd_pais] char(3) NOT NULL,
  [sg_uf] char(2) NOT NULL,
  [id_municipio] int(10) NOT NULL,
  [vl_equipamento] money(19,4),
  [nr_longitude] varchar(20),
  [cd_empresa_beneficiada] char(3) NOT NULL,
  [login_eq] varchar(50),
  [senha] varchar(50)
)
GO

CREATE TABLE [dbo].[erp_equipamento_contato] (
  [id_equipamento] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_equipamento_responsavel] (
  [id_equipamento] int(10) NOT NULL,
  [id_funcionario] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_fornecedor_contato] (
  [id_fornecedor] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_funcionario_contato] (
  [id_funcionario] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[erp_servico_contato] (
  [id_servico] int(10) NOT NULL,
  [id_contato] int(10) NOT NULL,
  [tp_contato] char(1) NOT NULL
)
GO

CREATE TABLE [dbo].[django_migrations] (
  [id] bigint(19) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [app] nvarchar(255) NOT NULL,
  [name] nvarchar(255) NOT NULL,
  [applied] datetimeoffset NOT NULL
)
GO

CREATE TABLE [dbo].[django_content_type] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [app_label] nvarchar(100) UNIQUE NOT NULL,
  [model] nvarchar(100) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[auth_permission] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [name] nvarchar(255) NOT NULL,
  [content_type_id] int(10) UNIQUE NOT NULL,
  [codename] nvarchar(100) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[auth_group] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [name] nvarchar(150) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[auth_group_permissions] (
  [id] bigint(19) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [group_id] int(10) UNIQUE NOT NULL,
  [permission_id] int(10) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[auth_user] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [password] nvarchar(128) NOT NULL,
  [last_login] datetimeoffset,
  [is_superuser] bit NOT NULL,
  [username] nvarchar(150) UNIQUE NOT NULL,
  [first_name] nvarchar(150) NOT NULL,
  [last_name] nvarchar(150) NOT NULL,
  [email] nvarchar(254) NOT NULL,
  [is_staff] bit NOT NULL,
  [is_active] bit NOT NULL,
  [date_joined] datetimeoffset NOT NULL
)
GO

CREATE TABLE [dbo].[auth_user_groups] (
  [id] bigint(19) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [user_id] int(10) UNIQUE NOT NULL,
  [group_id] int(10) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[auth_user_user_permissions] (
  [id] bigint(19) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [user_id] int(10) UNIQUE NOT NULL,
  [permission_id] int(10) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[django_admin_log] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [action_time] datetimeoffset NOT NULL,
  [object_id] nvarchar(MAX),
  [object_repr] nvarchar(200) NOT NULL,
  [action_flag] smallint(5) NOT NULL,
  [change_message] nvarchar(MAX) NOT NULL,
  [content_type_id] int(10),
  [user_id] int(10) NOT NULL
)
GO

CREATE TABLE [dbo].[django_session] (
  [session_key] nvarchar(40) PRIMARY KEY NOT NULL,
  [session_data] nvarchar(MAX) NOT NULL,
  [expire_date] datetimeoffset NOT NULL
)
GO

CREATE TABLE [dbo].[VeiculoSistemas] (
  [CodVei] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [CodSys] int(10),
  [NmoVei] nvarchar(1020),
  [PriVei] nvarchar(2),
  [VeiNacional] bit,
  [VeiOrdem] int(10),
  [CodTipoVei] int(10),
  [sg_uf] char(2),
  [tp_veiculo] char(3) NOT NULL,
  [st_veiculo] char(1),
  [end_veiculo] varchar(500),
  [no_identificador_url] varchar(100),
  [dt_ultima_noticia] datetime,
  [cd_usuario_web] char(60),
  [cd_senha_web] char(60),
  [cd_pais] nvarchar(6) NOT NULL,
  [cd_lingua] char(2),
  [vl_publicitario_cm] money(19,4),
  [cd_usuario_flip] char(60),
  [cd_senha_flip] char(60),
  [no_referencia] varchar(500),
  [end_flip] varchar(500),
  [id_municipio] int(10),
  [no_url_stream] varchar(4000),
  [in_domingo] char(1),
  [in_segunda] char(1),
  [in_terca] char(1),
  [in_quarta] char(1),
  [in_quinta] char(1),
  [in_sexta] char(1),
  [in_sabado] char(1),
  [st_url_stream] char(3),
  [qt_publico] int(10),
  [nr_telefone] varchar(30),
  [no_endereco] varchar(300),
  [dt_atualizacao] date,
  [tolerancia_sem_noticia] int(10),
  [qt_min_noticia] int(10),
  [periodo_publicacao] char(1),
  [tt_comando_encoder] varchar(2000),
  [cm_altura] decimal(6,2),
  [cm_largura] decimal(6,2),
  [json_lst_etiqueta] varchar(MAX),
  [in_extrair_texto_ocr] char(1),
  [modificado_por] int(10)
)
GO

CREATE TABLE [dbo].[municipio] (
  [id_municipio] int(10) PRIMARY KEY NOT NULL,
  [id_mesorregiao] tinyint(3) NOT NULL,
  [uf_municipio] char(2) NOT NULL,
  [no_municipio] nvarchar(100),
  [nr_latitude] float(53),
  [nr_longitude] float(53),
  [id_municipio_ibge] int(10)
)
GO

CREATE TABLE [dbo].[uf] (
  [sg_uf] char(2) PRIMARY KEY NOT NULL,
  [no_uf] nvarchar(100),
  [no_regiao] nvarchar(50) NOT NULL,
  [cd_uf_ibge] tinyint(3),
  [cd_pais] nvarchar(50),
  [id_capital] smallint(5),
  [nr_gmt] nvarchar(50)
)
GO

CREATE TABLE [dbo].[pais] (
  [cd_pais] nvarchar(6) PRIMARY KEY NOT NULL,
  [no_pais] nvarchar(200),
  [cd_pais_ibge] nvarchar(50) NOT NULL
)
GO

CREATE TABLE [dbo].[tipo_veiculo] (
  [tp_veiculo] char(3) PRIMARY KEY NOT NULL,
  [ds_tipo_veiculo] nvarchar(50) NOT NULL
)
GO

CREATE TABLE [dbo].[lingua] (
  [cd_lingua] char(2) PRIMARY KEY NOT NULL,
  [no_lingua] nvarchar(50)
)
GO

CREATE TABLE [dbo].[noticia_importada] (
  [cd_noticia] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_importacao] int(10),
  [dt_importacao] datetime NOT NULL,
  [dt_noticia] smalldatetime NOT NULL,
  [no_titulo] nvarchar(500),
  [tt_noticia] nvarchar(4000),
  [id_veiculo] int(10) NOT NULL,
  [ds_url] varchar(500) NOT NULL,
  [tt_sutia] varchar(1000),
  [id_editoria] int(10),
  [no_colunista] nvarchar(1000),
  [ds_url_media] varchar(2000),
  [cd_pagina] char(6),
  [clientes_relacionados] nvarchar(MAX),
  [categorias_relacionadas] nvarchar(MAX),
  [processado] bit DEFAULT (0),
  [imagem] nvarchar(255),
  [modificado_por] int(10)
)
GO

CREATE TABLE [dbo].[erp_cliente_old] (
  [id_cliente] smallint(5),
  [nr_cnpj] bigint(19),
  [nr_cpf] nvarchar(50),
  [no_cliente] nvarchar(100),
  [no_razao_social] nvarchar(100),
  [nr_insc_estadual] nvarchar(50),
  [no_endereco] nvarchar(300),
  [nr_telefone_gestor] nvarchar(50),
  [no_email_gestor] nvarchar(100),
  [no_contato_gestor] nvarchar(100),
  [no_contato_financeiro] nvarchar(100),
  [nr_telefone_financeiro] nvarchar(50),
  [no_email_financeiro] nvarchar(50),
  [no_contato_usuario] nvarchar(100),
  [nr_telefone_usuario] nvarchar(50),
  [no_email_usuario] nvarchar(50),
  [st_cliente] nvarchar(50),
  [dt_cadastro] datetime2,
  [nr_insc_municipal] nvarchar(50),
  [no_logradouro] nvarchar(250),
  [no_complemento] nvarchar(100),
  [no_bairro] nvarchar(50),
  [nr_endereco] nvarchar(50),
  [nr_cep] int(10),
  [cd_pais] nvarchar(50),
  [sg_uf] nvarchar(50),
  [id_municipio] smallint(5),
  [id_ultimo_servico_pago] nvarchar(50)
)
GO

CREATE TABLE [dbo].[erp_cliente] (
  [id_cliente] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [nr_cnpj] char(14),
  [nr_cpf] char(11),
  [no_cliente] varchar(100) NOT NULL,
  [no_razao_social] varchar(100),
  [nr_insc_estadual] char(14),
  [no_endereco] varchar(600),
  [nr_telefone_gestor] char(14),
  [no_email_gestor] varchar(80),
  [no_contato_gestor] varchar(80),
  [no_contato_financeiro] varchar(80),
  [nr_telefone_financeiro] char(14),
  [no_email_financeiro] varchar(80),
  [no_contato_usuario] varchar(80),
  [nr_telefone_usuario] char(14),
  [no_email_usuario] varchar(80),
  [st_cliente] char(1) NOT NULL,
  [dt_cadastro] datetime NOT NULL,
  [nr_insc_municipal] char(14),
  [no_logradouro] varchar(200),
  [no_complemento] varchar(100),
  [no_bairro] varchar(40),
  [nr_endereco] char(10),
  [nr_cep] char(8),
  [cd_pais] char(3),
  [sg_uf] char(2),
  [id_municipio] int(10),
  [id_ultimo_servico_pago] int(10),
  [sigla_cliente] nvarchar(20),
  [modificado_por] int(10)
)
GO

CREATE TABLE [dbo].[erp_contrato] (
  [id_contrato] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) NOT NULL,
  [cd_empresa] char(3) NOT NULL,
  [cd_identificacao] char(20),
  [descricao_contrato] varchar(1000) NOT NULL,
  [data_inicio_vigencia] date NOT NULL,
  [data_fim_vigencia] date NOT NULL,
  [tipo_prorrogacao] char(3) NOT NULL,
  [descricao_objeto] varchar(MAX) NOT NULL,
  [informacao_adicional] varchar(MAX),
  [valor_contrato] money(19,4) NOT NULL,
  [dia_emissao_nota_fiscal] int(10) NOT NULL,
  [status_contrato] char(1) NOT NULL,
  [in_contrato_assinado] bit NOT NULL,
  [tipo_cobranca] char(3) NOT NULL,
  [data_cadastro] datetime NOT NULL,
  [dia_do_pagamento] int(10) NOT NULL,
  [dia_aviso_fim_vigencia] int(10),
  [forma_envio_nf] char(1),
  [modificado_por] int(10)
)
GO

CREATE TABLE [dbo].[erp_produto] (
  [cd_produto] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [descricao] nvarchar(100) NOT NULL,
  [situacao_produto] bit NOT NULL,
  [cd_produto_principal] int(10)
)
GO

CREATE TABLE [dbo].[erp_produto_veiculos] (
  [id] bigint(19) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [erpproduto_id] int(10) UNIQUE NOT NULL,
  [veiculosistemas_id] int(10) UNIQUE NOT NULL
)
GO

CREATE TABLE [dbo].[CategoriaPalavraChave] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [nome] nvarchar(510) UNIQUE,
  [id_cliente] int(10),
  [status] bit DEFAULT (1)
)
GO

CREATE TABLE [dbo].[PalavraChave] (
  [id] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) UNIQUE NOT NULL,
  [id_categoria] int(10) UNIQUE NOT NULL,
  [palavra] nvarchar(510) UNIQUE,
  [data_cadastro] datetime DEFAULT (getdate()),
  [status] bit DEFAULT (1)
)
GO

CREATE TABLE [dbo].[noticia_importada_backup] (
  [cd_noticia] int(10) NOT NULL IDENTITY(1, 1),
  [id_importacao] int(10),
  [dt_importacao] datetime NOT NULL,
  [dt_noticia] smalldatetime NOT NULL,
  [no_titulo] varchar(500) NOT NULL,
  [tt_noticia] varchar(MAX) NOT NULL,
  [id_veiculo] int(10) NOT NULL,
  [ds_url] varchar(500) NOT NULL,
  [tt_sutia] varchar(1000),
  [id_editoria] int(10),
  [no_colunista] varchar(1000),
  [ds_url_media] varchar(2000),
  [cd_pagina] char(6),
  [clientes_relacionados] nvarchar(MAX),
  [categorias_relacionadas] nvarchar(MAX),
  [processado] bit
)
GO

CREATE TABLE [dbo].[contato_cliente] (
  [id_contato] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) NOT NULL,
  [nome] nvarchar(255) NOT NULL,
  [email] nvarchar(255) NOT NULL,
  [telefone] nvarchar(20)
)
GO

CREATE TABLE [dbo].[envio_email] (
  [id_envio] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) NOT NULL,
  [nome_disparo] nvarchar(255) NOT NULL,
  [data_agendamento] datetime NOT NULL,
  [categorias] nvarchar(MAX) NOT NULL,
  [veiculos] nvarchar(MAX) NOT NULL,
  [status] nvarchar(50) NOT NULL DEFAULT 'Pendente'
)
GO

CREATE TABLE [dbo].[sites_cliente] (
  [id_site] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) NOT NULL,
  [nome_site] nvarchar(255) NOT NULL,
  [dominio] nvarchar(255) UNIQUE NOT NULL,
  [cor_primaria] nvarchar(7) NOT NULL DEFAULT '#000000',
  [cor_secundaria] nvarchar(7) NOT NULL DEFAULT '#FFFFFF',
  [logotipo] nvarchar(255),
  [data_criacao] datetime DEFAULT (getdate())
)
GO

CREATE TABLE [dbo].[Evento] (
  [id_evento] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) NOT NULL,
  [descricao] nvarchar(255) NOT NULL,
  [data_hora] datetime DEFAULT (getdate()),
  [id_usuario] int(10),
  [content_type_id] int(10) NOT NULL,
  [object_id] int(10) NOT NULL,
  [acao] nvarchar(20) NOT NULL
)
GO

CREATE TABLE [dbo].[configuracao_cliente] (
  [id_configuracao] int(10) PRIMARY KEY NOT NULL IDENTITY(1, 1),
  [id_cliente] int(10) UNIQUE NOT NULL,
  [nome_cliente_sistema] nvarchar(510) NOT NULL,
  [id_empresa_prestadora] char(3) NOT NULL,
  [logotipo] nvarchar(510),
  [cor_primaria] nvarchar(14) NOT NULL DEFAULT '#000000',
  [cor_secundaria] nvarchar(14) NOT NULL DEFAULT '#FFFFFF',
  [sigla_cliente] varchar(10) NOT NULL,
  [url_pagina_cliente] varchar(255),
  [status_pagina] char(1) NOT NULL DEFAULT 'I',
  [data_ativacao] datetime
)
GO

CREATE INDEX [auth_permission_content_type_id_2f476e4b] ON [dbo].[auth_permission] ("content_type_id")
GO

CREATE INDEX [auth_group_permissions_group_id_b120cbf9] ON [dbo].[auth_group_permissions] ("group_id")
GO

CREATE INDEX [auth_group_permissions_permission_id_84c5c92e] ON [dbo].[auth_group_permissions] ("permission_id")
GO

CREATE INDEX [auth_user_groups_group_id_97559544] ON [dbo].[auth_user_groups] ("group_id")
GO

CREATE INDEX [auth_user_groups_user_id_6a12ed8b] ON [dbo].[auth_user_groups] ("user_id")
GO

CREATE INDEX [auth_user_user_permissions_permission_id_1fbb5f2c] ON [dbo].[auth_user_user_permissions] ("permission_id")
GO

CREATE INDEX [auth_user_user_permissions_user_id_a95ead1b] ON [dbo].[auth_user_user_permissions] ("user_id")
GO

CREATE INDEX [django_admin_log_content_type_id_c4bce8eb] ON [dbo].[django_admin_log] ("content_type_id")
GO

CREATE INDEX [django_admin_log_user_id_c564eba6] ON [dbo].[django_admin_log] ("user_id")
GO

CREATE INDEX [django_session_expire_date_a5c62663] ON [dbo].[django_session] ("expire_date")
GO

CREATE INDEX [idx_noticia_data] ON [dbo].[noticia_importada] ("id_veiculo", "cd_pagina", "dt_noticia")
GO

CREATE INDEX [idx_noticia_titulo] ON [dbo].[noticia_importada] ("no_titulo")
GO

CREATE INDEX [idx_noticia_veiculo] ON [dbo].[noticia_importada] ("cd_pagina", "id_veiculo")
GO

CREATE INDEX [idx_processado] ON [dbo].[noticia_importada] ("processado")
GO

CREATE INDEX [erp_produto_cd_produto_principal_ed8fcb7c] ON [dbo].[erp_produto] ("cd_produto_principal")
GO

CREATE INDEX [erp_produto_veiculos_erpproduto_id_b9ff0c14] ON [dbo].[erp_produto_veiculos] ("erpproduto_id")
GO

CREATE INDEX [erp_produto_veiculos_veiculosistemas_id_3ae7ab8d] ON [dbo].[erp_produto_veiculos] ("veiculosistemas_id")
GO

CREATE INDEX [idx_url_pagina_cliente] ON [dbo].[configuracao_cliente] ("url_pagina_cliente")
GO

ALTER TABLE [dbo].[auth_group_permissions] ADD CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id] FOREIGN KEY ([permission_id]) REFERENCES [dbo].[auth_permission] ([id])
GO

ALTER TABLE [dbo].[auth_group_permissions] ADD CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id] FOREIGN KEY ([group_id]) REFERENCES [dbo].[auth_group] ([id])
GO

ALTER TABLE [dbo].[auth_permission] ADD CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id] FOREIGN KEY ([content_type_id]) REFERENCES [dbo].[django_content_type] ([id])
GO

ALTER TABLE [dbo].[auth_user_groups] ADD CONSTRAINT [auth_user_groups_group_id_97559544_fk_auth_group_id] FOREIGN KEY ([group_id]) REFERENCES [dbo].[auth_group] ([id])
GO

ALTER TABLE [dbo].[auth_user_groups] ADD CONSTRAINT [auth_user_groups_user_id_6a12ed8b_fk_auth_user_id] FOREIGN KEY ([user_id]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[auth_user_user_permissions] ADD CONSTRAINT [auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id] FOREIGN KEY ([user_id]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[auth_user_user_permissions] ADD CONSTRAINT [auth_user_user_permissions_permission_id_1fbb5f2c_fk_auth_permission_id] FOREIGN KEY ([permission_id]) REFERENCES [dbo].[auth_permission] ([id])
GO

ALTER TABLE [dbo].[CategoriaPalavraChave] ADD CONSTRAINT [fk_categoria_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[configuracao_cliente] ADD CONSTRAINT [fk_configuracao_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[configuracao_cliente] ADD CONSTRAINT [fk_configuracao_empresa] FOREIGN KEY ([id_empresa_prestadora]) REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO

ALTER TABLE [dbo].[contato_cliente] ADD CONSTRAINT [fk_contato_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente]) ON DELETE CASCADE
GO

ALTER TABLE [dbo].[django_admin_log] ADD CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id] FOREIGN KEY ([content_type_id]) REFERENCES [dbo].[django_content_type] ([id])
GO

ALTER TABLE [dbo].[django_admin_log] ADD CONSTRAINT [django_admin_log_user_id_c564eba6_fk_auth_user_id] FOREIGN KEY ([user_id]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[envio_email] ADD CONSTRAINT [fk_envio_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[erp_cliente] ADD CONSTRAINT [FK_erp_cliente_municipio] FOREIGN KEY ([id_municipio]) REFERENCES [dbo].[municipio] ([id_municipio])
GO

ALTER TABLE [dbo].[erp_cliente] ADD CONSTRAINT [FK_erp_cliente_uf] FOREIGN KEY ([sg_uf]) REFERENCES [dbo].[uf] ([sg_uf])
GO

ALTER TABLE [dbo].[erp_cliente] ADD CONSTRAINT [FK_erp_cliente_modificado] FOREIGN KEY ([modificado_por]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[erp_contrato] ADD CONSTRAINT [FK_erp_contrato_modificado] FOREIGN KEY ([modificado_por]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[erp_contrato] ADD CONSTRAINT [FK_erp_contrato_erp_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[erp_contrato] ADD CONSTRAINT [FK_erp_contrato_erp_empresa] FOREIGN KEY ([cd_empresa]) REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO

ALTER TABLE [dbo].[erp_empresa] ADD CONSTRAINT [FK_erp_empresa_modificado] FOREIGN KEY ([modificado_por]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[erp_empresa] ADD CONSTRAINT [FK_erp_empresa_municipio] FOREIGN KEY ([id_municipio]) REFERENCES [dbo].[municipio] ([id_municipio])
GO

ALTER TABLE [dbo].[erp_produto] ADD CONSTRAINT [erp_produto_cd_produto_principal_ed8fcb7c_fk_erp_produto_cd_produto] FOREIGN KEY ([cd_produto_principal]) REFERENCES [dbo].[erp_produto] ([cd_produto])
GO

ALTER TABLE [dbo].[erp_produto_veiculos] ADD CONSTRAINT [erp_produto_veiculos_erpproduto_id_b9ff0c14_fk_erp_produto_cd_produto] FOREIGN KEY ([erpproduto_id]) REFERENCES [dbo].[erp_produto] ([cd_produto])
GO

ALTER TABLE [dbo].[erp_produto_veiculos] ADD CONSTRAINT [erp_produto_veiculos_veiculosistemas_id_3ae7ab8d_fk_VeiculoSistemas_CodVei] FOREIGN KEY ([veiculosistemas_id]) REFERENCES [dbo].[VeiculoSistemas] ([CodVei])
GO

ALTER TABLE [dbo].[Evento] ADD CONSTRAINT [fk_evento_usuario] FOREIGN KEY ([id_usuario]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[Evento] ADD CONSTRAINT [FK_evento_content_type] FOREIGN KEY ([content_type_id]) REFERENCES [dbo].[django_content_type] ([id])
GO

ALTER TABLE [dbo].[Evento] ADD CONSTRAINT [FK__Evento__id_clien__6E565CE8] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[InstallSistemas] ADD CONSTRAINT [FK_InstallSistemas_erp_empresa] FOREIGN KEY ([cd_empresa]) REFERENCES [dbo].[erp_empresa] ([cd_empresa])
GO

ALTER TABLE [dbo].[InstallSistemas] ADD CONSTRAINT [FK_InstallSistemas_erp_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[municipio] ADD CONSTRAINT [FK_municipio_uf] FOREIGN KEY ([uf_municipio]) REFERENCES [dbo].[uf] ([sg_uf])
GO

ALTER TABLE [dbo].[noticia_importada] ADD CONSTRAINT [FK_noticia_importada_VeiculoSistemas] FOREIGN KEY ([id_veiculo]) REFERENCES [dbo].[VeiculoSistemas] ([CodVei])
GO

ALTER TABLE [dbo].[noticia_importada] ADD CONSTRAINT [FK_noticia_importada_modificado] FOREIGN KEY ([modificado_por]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[PalavraChave] ADD CONSTRAINT [FK__PalavraCh__id_ca__1A9EF37A] FOREIGN KEY ([id_categoria]) REFERENCES [dbo].[CategoriaPalavraChave] ([id])
GO

ALTER TABLE [dbo].[PalavraChave] ADD CONSTRAINT [FK__PalavraCh__id_cl__19AACF41] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente])
GO

ALTER TABLE [dbo].[sites_cliente] ADD CONSTRAINT [fk_site_cliente] FOREIGN KEY ([id_cliente]) REFERENCES [dbo].[erp_cliente] ([id_cliente]) ON DELETE CASCADE
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_uf] FOREIGN KEY ([sg_uf]) REFERENCES [dbo].[uf] ([sg_uf])
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_pais] FOREIGN KEY ([cd_pais]) REFERENCES [dbo].[pais] ([cd_pais])
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_tipo_veiculo] FOREIGN KEY ([tp_veiculo]) REFERENCES [dbo].[tipo_veiculo] ([tp_veiculo])
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_lingua] FOREIGN KEY ([cd_lingua]) REFERENCES [dbo].[lingua] ([cd_lingua])
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_modificado] FOREIGN KEY ([modificado_por]) REFERENCES [dbo].[auth_user] ([id])
GO

ALTER TABLE [dbo].[VeiculoSistemas] ADD CONSTRAINT [FK_VeiculoSistemas_Municipio] FOREIGN KEY ([id_municipio]) REFERENCES [dbo].[municipio] ([id_municipio])
GO
