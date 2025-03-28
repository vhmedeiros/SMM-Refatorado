USE [bdNewsUp]
GO
/****** Object:  StoredProcedure [dbo].[VincularNoticiasAClientes]    Script Date: 26/03/2025 09:56:53 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[VincularNoticiasAClientes]
AS
BEGIN
    SET NOCOUNT ON;

    -- Criar tabela temporária com notícias não processadas (em lote)
    CREATE TABLE #NoticiasLote (
        id_noticia INT
    );

    -- Pegar até 1000 notícias não processadas
    INSERT INTO #NoticiasLote (id_noticia)
    SELECT TOP 1000 cd_noticia
    FROM noticia_importada
    WHERE processado = 0
    ORDER BY dt_importacao;

    -- Tabela temporária para armazenar relações cliente-categoria
    CREATE TABLE #NoticiasRelacionadas (
        id_noticia INT,
        id_cliente INT,
        id_categoria INT
    );

    DECLARE @Palavras NVARCHAR(MAX) = '';

    -- Tabela para armazenar palavras-chave com mesma collation
    CREATE TABLE #PalavrasTemp (
        palavra NVARCHAR(255) COLLATE SQL_Latin1_General_CP1_CI_AS
    );

    -- Inserir palavras válidas
    INSERT INTO #PalavrasTemp (palavra)
    SELECT palavra COLLATE SQL_Latin1_General_CP1_CI_AS
    FROM PalavraChave
    WHERE palavra COLLATE SQL_Latin1_General_CP1_CI_AS NOT IN (
        SELECT stopword COLLATE SQL_Latin1_General_CP1_CI_AS
        FROM sys.fulltext_system_stopwords
        WHERE language_id = 1046
    );

    -- Gerar string de palavras para CONTAINS
    SELECT @Palavras = STRING_AGG('"' + palavra + '"', ' OR ')
    FROM #PalavrasTemp;

    IF @Palavras IS NOT NULL AND LEN(@Palavras) > 0
    BEGIN
        DECLARE @SQL NVARCHAR(MAX);

        -- Montar SQL dinâmico para filtrar apenas as notícias do lote
        SET @SQL = '
            INSERT INTO #NoticiasRelacionadas (id_noticia, id_cliente, id_categoria)
            SELECT DISTINCT n.cd_noticia, p.id_cliente, p.id_categoria
            FROM noticia_importada n
            INNER JOIN PalavraChave p ON
                (CONTAINS(n.no_titulo, ''' + @Palavras + ''') OR
                 CONTAINS(n.tt_noticia, ''' + @Palavras + '''))
            INNER JOIN #NoticiasLote l ON n.cd_noticia = l.id_noticia;
        ';

        EXEC sp_executesql @SQL;
    END

    -- Atualizar os campos da notícia com clientes e categorias
    UPDATE n
    SET 
        clientes_relacionados = STUFF((
            SELECT DISTINCT ',' + CAST(r.id_cliente AS NVARCHAR)
            FROM #NoticiasRelacionadas r
            WHERE r.id_noticia = n.cd_noticia
            FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, ''),
        
        categorias_relacionadas = STUFF((
            SELECT DISTINCT ',' + CAST(r.id_categoria AS NVARCHAR)
            FROM #NoticiasRelacionadas r
            WHERE r.id_noticia = n.cd_noticia
            FOR XML PATH(''), TYPE).value('.', 'NVARCHAR(MAX)'), 1, 1, ''),

        processado = 1
    FROM noticia_importada n
    WHERE EXISTS (
        SELECT 1 FROM #NoticiasRelacionadas r WHERE r.id_noticia = n.cd_noticia
    );

    DROP TABLE #NoticiasLote;
    DROP TABLE #NoticiasRelacionadas;
    DROP TABLE #PalavrasTemp;
END;
GO
