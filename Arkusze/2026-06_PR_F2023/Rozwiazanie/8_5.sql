SELECT TOP 1 Oceny.Id_Ucznia FROM Oceny INNER JOIN Kategorie
ON Oceny.Id_Kategorii = Kategorie.Id_Kategorii
WHERE Oceny.Ocena = 6 AND Kategorie.Nazwa_kategorii = "sprawdzian"
GROUP BY Oceny.Id_Ucznia ORDER BY COUNT(Oceny.Id_Oceny) DESC;