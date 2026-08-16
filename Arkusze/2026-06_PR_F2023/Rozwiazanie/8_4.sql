SELECT Kategorie.Nazwa_Kategorii, COUNT(Oceny.Id_Oceny)
FROM Kategorie INNER JOIN Oceny
ON Kategorie.Id_Kategorii = Oceny.Id_Kategorii
GROUP BY Kategorie.Nazwa_Kategorii;