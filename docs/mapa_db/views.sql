USE [bdNewsUp]
GO
/****** Object:  View [dbo].[vw_contato]    Script Date: 26/03/2025 09:56:14 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE view [dbo].[vw_contato]   
as  
select   
   c.id_contato            ,  
   c.no_contato            ,  
   c.st_contato            ,  
   c.no_departamento       ,  
   c.no_cargo              ,  
   c.no_endereco           ,  
   c.nr_telefone_trabalho  ,  
   c.nr_telefone_celular   ,  
   c.nr_telefone_particular,  
   c.no_email_trabalho     ,  
   c.no_email_particular   ,  
   c.tt_observacao         ,  
   cc.id_cliente,  
   f.id_fornecedor,  
   fc.id_funcionario,
   ec.id_equipamento,
   sc.id_servico,
   ctc.id_contrato
from erp_contato c  
left join erp_cliente_contato cc on  
   c.id_contato = cc.id_contato  
left join erp_fornecedor_contato f on  
   c.id_contato = f.id_contato  
left join erp_funcionario_contato fc on  
   c.id_contato = fc.id_contato
left join erp_equipamento_contato ec on  
   c.id_contato = ec.id_contato
left join erp_servico_contato sc on  
   c.id_contato = sc.id_contato
left join erp_contrato_contato ctc on  
   c.id_contato = ctc.id_contato


GO
