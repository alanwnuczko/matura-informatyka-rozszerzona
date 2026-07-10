SELECT DISTINCT
Produkty.IdProduktu, 
Produkty.Nazwa
FROM 
Kategorie
JOIN Produkty ON Kategorie.IdKategorii = Produkty.IdKategorii
JOIN Opis_transakcji ON Produkty.IdProduktu = Opis_transakcji.IdProduktu
WHERE
Kategorie.NazwaKategorii = 'spozywcze'
AND Produkty.Opis LIKE '%do ekspresu kolbowego%';