# Operatory

## Porównania

**Operatory:**
- `=` – równe
- `<>` – różne
- `>` – większe
- `<` – mniejsze
- `>=` – większe lub równe
- `<=` – mniejsze lub równe

**Opis:**
Służą do porównywania wartości w warunku `WHERE`.

**Przykłady:**
```sql
WHERE Wiek = 18;
WHERE Klasa <> "4A";
WHERE Punkty > 50;
WHERE Wiek < 18;
WHERE Punkty >= 50;
WHERE Wiek <= 18;
```

## Logiczne

**Operatory:**
- `AND` – wszystkie warunki muszą być spełnione
- `OR` – co najmniej jeden warunek musi spełniony
- `NOT` – odwraca wynik warunku

**Przykłady:**
```sql
WHERE Klasa = "4A" AND Punkty >= 50;

WHERE Klasa = "4A" OR Klasa = "4B";

WHERE NOT Klasa = "4A";
```

## Pozostałe

**Operatory:**
- `LIKE` – wyszukuje wartości pasujące do określonego wzorca (np. tekst zaczynający się od danej litery)
- `IN` – sprawdza, czy wartość należy do zbioru
- `BETWEEN` – sprawdza, czy wartość znajduje się w przedziale
- `IS NULL` – sprawdza, czy wartość jest pusta (`NULL`)

**Przykłady:**
```sql
WHERE Nazwisko LIKE "K*";

WHERE Klasa IN ("4A", "4B");

WHERE Punkty BETWEEN 50 AND 100;

WHERE Telefon IS NULL;
```