USE [bdNewsUp]
GO
/****** Object:  UserDefinedFunction [dbo].[RemoverAcentos]    Script Date: 26/03/2025 09:57:43 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE FUNCTION [dbo].[RemoverAcentos] (@Texto NVARCHAR(MAX))
RETURNS NVARCHAR(MAX)
AS
BEGIN
    DECLARE @Resultado NVARCHAR(MAX)
    SET @Resultado = @Texto

    -- Substituir caracteres acentuados por não acentuados
    SET @Resultado = REPLACE(@Resultado, 'á', 'a')
    SET @Resultado = REPLACE(@Resultado, 'à', 'a')
    SET @Resultado = REPLACE(@Resultado, 'ã', 'a')
    SET @Resultado = REPLACE(@Resultado, 'â', 'a')
    SET @Resultado = REPLACE(@Resultado, 'ä', 'a')
    SET @Resultado = REPLACE(@Resultado, 'é', 'e')
    SET @Resultado = REPLACE(@Resultado, 'è', 'e')
    SET @Resultado = REPLACE(@Resultado, 'ê', 'e')
    SET @Resultado = REPLACE(@Resultado, 'ë', 'e')
    SET @Resultado = REPLACE(@Resultado, 'í', 'i')
    SET @Resultado = REPLACE(@Resultado, 'ì', 'i')
    SET @Resultado = REPLACE(@Resultado, 'î', 'i')
    SET @Resultado = REPLACE(@Resultado, 'ï', 'i')
    SET @Resultado = REPLACE(@Resultado, 'ó', 'o')
    SET @Resultado = REPLACE(@Resultado, 'ò', 'o')
    SET @Resultado = REPLACE(@Resultado, 'õ', 'o')
    SET @Resultado = REPLACE(@Resultado, 'ô', 'o')
    SET @Resultado = REPLACE(@Resultado, 'ö', 'o')
    SET @Resultado = REPLACE(@Resultado, 'ú', 'u')
    SET @Resultado = REPLACE(@Resultado, 'ù', 'u')
    SET @Resultado = REPLACE(@Resultado, 'û', 'u')
    SET @Resultado = REPLACE(@Resultado, 'ü', 'u')
    SET @Resultado = REPLACE(@Resultado, 'ç', 'c')
    SET @Resultado = REPLACE(@Resultado, 'Á', 'A')
    SET @Resultado = REPLACE(@Resultado, 'À', 'A')
    SET @Resultado = REPLACE(@Resultado, 'Ã', 'A')
    SET @Resultado = REPLACE(@Resultado, 'Â', 'A')
    SET @Resultado = REPLACE(@Resultado, 'Ä', 'A')
    SET @Resultado = REPLACE(@Resultado, 'É', 'E')
    SET @Resultado = REPLACE(@Resultado, 'È', 'E')
    SET @Resultado = REPLACE(@Resultado, 'Ê', 'E')
    SET @Resultado = REPLACE(@Resultado, 'Ë', 'E')
    SET @Resultado = REPLACE(@Resultado, 'Í', 'I')
    SET @Resultado = REPLACE(@Resultado, 'Ì', 'I')
    SET @Resultado = REPLACE(@Resultado, 'Î', 'I')
    SET @Resultado = REPLACE(@Resultado, 'Ï', 'I')
    SET @Resultado = REPLACE(@Resultado, 'Ó', 'O')
    SET @Resultado = REPLACE(@Resultado, 'Ò', 'O')
    SET @Resultado = REPLACE(@Resultado, 'Õ', 'O')
    SET @Resultado = REPLACE(@Resultado, 'Ô', 'O')
    SET @Resultado = REPLACE(@Resultado, 'Ö', 'O')
    SET @Resultado = REPLACE(@Resultado, 'Ú', 'U')
    SET @Resultado = REPLACE(@Resultado, 'Ù', 'U')
    SET @Resultado = REPLACE(@Resultado, 'Û', 'U')
    SET @Resultado = REPLACE(@Resultado, 'Ü', 'U')
    SET @Resultado = REPLACE(@Resultado, 'Ç', 'C')

    RETURN @Resultado
END
GO
