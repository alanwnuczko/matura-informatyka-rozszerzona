SELECT DISTINCT Producent.nazwa FROM Producent
INNER JOIN Laziki ON Producent.kod_producenta = Laziki.kod_producenta
INNER JOIN Pomiary ON Laziki.nr_lazika = Pomiary.nr_lazika
INNER JOIN Obszary ON Pomiary.kod_obszaru = Obszary.kod_obszaru WHERE Obszary.nazwa_obszaru = "Arcadia" AND YEAR(Pomiary.data_pomiaru) = 2060;