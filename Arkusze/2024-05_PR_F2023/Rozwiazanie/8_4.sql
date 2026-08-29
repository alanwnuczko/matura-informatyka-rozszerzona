SELECT IdFotoradaru FROM Fotoradar
WHERE IdFotoradaru NOT IN (SELECT Rejestr.IdFotoradaru
FROM Rejestr
WHERE IdFotoradaru IS NOT NULL);