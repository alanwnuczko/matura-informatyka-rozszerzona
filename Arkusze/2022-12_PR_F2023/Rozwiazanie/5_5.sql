SELECT Klienci.imie, Klienci.nazwisko, Sum(uslugi_dodatkowe.cena_uslugi)
FROM Klienci, Noclegi, uslugi_dodatkowe
WHERE Klienci.nr_dowodu = Noclegi.nr_dowodu AND Noclegi.id_pobytu = Uslugi.id_pobytu
GROUP BY Klienci.imie, Klienci.nazwisko;