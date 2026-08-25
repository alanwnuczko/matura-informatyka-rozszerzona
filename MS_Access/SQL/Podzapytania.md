# Podzapytania

## IN z podzapytaniem

**Składnia:**
```sql
SELECT kolumny
FROM tabela
WHERE kolumna IN (SELECT kolumna FROM inna_tabela WHERE warunek);
```

**Opis:**
Filtruje rekordy, których wartość w wybranej kolumnie znajduje się w zbiorze wartości zwróconych przez podzapytanie.

**Przykład:**
```sql
SELECT Imie, Nazwisko
FROM Klienci
WHERE IdKlienta IN (SELECT IdKlienta FROM Zamowienia WHERE Wartosc > 1000);
```

**Wynik:**
Zwraca klientów, którzy złożyli co najmniej jedno zamówienie o wartości powyżej 1000 zł.

## NOT IN z podzapytaniem

**Składnia:**
```sql
SELECT kolumny
FROM tabela
WHERE kolumna NOT IN (SELECT kolumna FROM inna_tabela);
```

**Opis:**
Wybiera rekordy, których wartość **nie występuje** w zbiorze wartości zwróconych przez podzapytanie.

**Przykład:**
```sql
SELECT Tytul
FROM Ksiazki
WHERE IdKsiazki NOT IN (SELECT IdKsiazki FROM Wypozyczenia);
```

**Wynik:**
Zwraca tytuły książek, które nigdy nie zostały wypożyczone.

## Porównanie z funkcją agregującą

**Składnia:**
```sql
SELECT kolumny
FROM tabela
WHERE kolumna > (SELECT AVG(kolumna) FROM tabela);
```

**Opis:**
Porównuje wartość kolumny z pojedynczą wartością skalarną obliczoną przez podzapytanie (np. średnią, minimum, maksimum).

**Przykład:**
```sql
SELECT NazwaProduktu, Cena
FROM Produkty
WHERE Cena > (SELECT AVG(Cena) FROM Produkty);
```

**Wynik:**
Zwraca produkty, których cena jest wyższa od średniej ceny wszystkich produktów.
