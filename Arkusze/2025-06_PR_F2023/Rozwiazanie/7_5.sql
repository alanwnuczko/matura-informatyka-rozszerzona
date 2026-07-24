SELECT DISTINCT Wizyty.id_klienta FROM Wizyty
INNER JOIN Fryzjerzy ON
Wizyty.id_fryzjera = Fryzjerzy.id_fryzjera
INNER JOIN Salony ON
Fryzjerzy.id_salonu = Salony.id_salonu
WHERE Salony.nazwa_salonu LIKE "Magnolia";