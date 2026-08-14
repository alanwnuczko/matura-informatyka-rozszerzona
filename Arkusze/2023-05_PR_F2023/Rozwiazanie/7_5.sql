SELECT SUM(Sklep.cena)
FROM Gry INNER JOIN Sklep On Gry.id_gry = Sklep.id_gry
WHERE Gry.kategoria = 'logiczna' AND Sklep.promocja = TRUE;