SELECT DISTINCT Statki.Nazwa_statku
FROM (Armator INNER JOIN Przybycia ON Armator.Id_Armatora = Przybycia.Id_Armatora)
INNER JOIN Statki ON Przybycia.Nr_IMO = Statki.Nr_IMO
WHERE Armator.Armator = "XYZ";