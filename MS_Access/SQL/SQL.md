# SQL w MS Access

## SELECT

**Składnia:**
```sql
SELECT kolumna1, kolumna2
FROM tabela;
```

**Opis:**
Wyświetla wybrane kolumny z tabeli.

**Przykład:**
```sql
SELECT Imie, Nazwisko
FROM Uczniowie;
```

## TOP

**Składnia:**
```sql
SELECT TOP liczba *
FROM tabela;
```

**Opis:**
Zwraca określoną liczbę pierwszych rekordów z wyniku zapytania.

**Przykład:**
```sql
SELECT TOP 1 *
FROM Uczniowie
ORDER BY Punkty DESC;
```

**Wynik:**
Zwraca rekord ucznia z największą liczbą punktów.

## DISTINCT

**Składnia:**
```sql
SELECT DISTINCT kolumna
FROM tabela;
```

**Opis:**
Wyświetla tylko unikalne wartości.

**Przykład:**
```sql
SELECT DISTINCT Klasa
FROM Uczniowie;
```

## WHERE

**Składnia:**
```sql
SELECT *
FROM tabela
WHERE warunek;
```

**Opis:**
Filtruje rekordy spełniające warunek.

**Przykład:**
```sql
SELECT *
FROM Uczniowie
WHERE Klasa = "4A";
```

## ORDER BY

**Składnia:**
```sql
SELECT *
FROM tabela
ORDER BY kolumna ASC;
```

**Opis:**
Sortuje wyniki.
- `ASC` – sortowanie rosnące (od najmniejszej wartości do największej, domyślne)
- `DESC` – sortowanie malejące (od największej wartości do najmniejszej)

**Przykład:**
```sql
SELECT *
FROM Uczniowie
ORDER BY Nazwisko ASC;
```

## GROUP BY

**Składnia:**
```sql
SELECT kolumna, funkcja(kolumna)
FROM tabela
GROUP BY kolumna;
```

**Opis:**
Grupuje rekordy.

**Przykład:**
```sql
SELECT Klasa, COUNT(*)
FROM Uczniowie
GROUP BY Klasa;
```

## HAVING

**Składnia:**
```sql
SELECT kolumna, funkcja(kolumna)
FROM tabela
GROUP BY kolumna
HAVING warunek;
```

**Opis:**
Filtruje grupy utworzone przez `GROUP BY`.

**Przykład:**
```sql
SELECT Klasa, COUNT(*)
FROM Uczniowie
GROUP BY Klasa
HAVING COUNT(*) > 20;
```

## INNER JOIN

**Składnia:**
```sql
SELECT *
FROM tabela1
INNER JOIN tabela2
ON tabela1.id = tabela2.id;
```

**Opis:**
Łączy rekordy występujące w obu tabelach.

**Przykład:**
```sql
SELECT Uczniowie.Imie, Klasy.Nazwa
FROM Uczniowie
INNER JOIN Klasy
ON Uczniowie.IdKlasy = Klasy.IdKlasy;
```

## LEFT JOIN

**Składnia:**
```sql
SELECT *
FROM tabela1
LEFT JOIN tabela2
ON tabela1.id = tabela2.id;
```

**Opis:**
Wyświetla wszystkie rekordy z lewej tabeli oraz pasujące z prawej.

**Przykład:**
```sql
SELECT Uczniowie.Imie, Klasy.Nazwa
FROM Uczniowie
LEFT JOIN Klasy
ON Uczniowie.IdKlasy = Klasy.IdKlasy;
```
---

## Kolejność zapisu:
```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY;
```