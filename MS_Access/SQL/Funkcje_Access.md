# Funkcje MS Access SQL

## IIf

**Składnia:**
```sql
IIf(warunek, wartość_gdy_prawda, wartość_gdy_fałsz)
```

**Opis:**
Zwraca jedną z dwóch wartości w zależności od wyniku warunku logicznego. Jest to odpowiednik funkcji `JEŻELI` w Excelu.

**Przykład:**
```sql
SELECT Imie, Nazwisko, IIf(Wiek >= 18, "Pełnoletni", "Niepełnoletni") AS Status
FROM Uczniowie;
```

**Wynik:**
Tworzy kolumnę `Status` o wartości „Pełnoletni” lub „Niepełnoletni”.

## Nz

**Składnia:**
```sql
Nz(wartość, [wartość_gdy_null])
```

**Opis:**
Zastępuje wartość `NULL` określoną wartością domyślną. Jeśli drugi argument zostanie pominięty, zwraca `0` dla liczb lub pusty ciąg `""` dla tekstu.

**Przykład:**
```sql
SELECT Imie, Nz(Punkty, 0) AS PunktyBezNull
FROM Wyniki;
```

**Wynik:**
Dla rekordów, gdzie `Punkty` to `NULL`, zwraca liczbę `0`.

## Year, Month, Day

**Składnia:**
```sql
Year(data)
Month(data)
Day(data)
```

**Opis:**
Wyciąga z daty odpowiednio rok (np. 2026), numer miesiąca (1-12) lub numer dnia miesiąca (1-31).

**Przykład:**
```sql
SELECT Imie, Nazwisko, DataUrodzenia
FROM Uczniowie
WHERE Year(DataUrodzenia) = 2005;
```

**Wynik:**
Zwraca uczniów urodzonych w 2005 roku.

## DateDiff

**Składnia:**
```sql
DateDiff("interwał", data1, data2)
```

**Opis:**
Zwraca różnicę jednostek czasu między dwiema datami (`data2 - data1`).

**Interwały:**
- `"d"` - dni
- `"m"` - miesiące
- `"yyyy"` - lata
- `"ww"` - tygodnie

**Przykład:**
```sql
SELECT IdWypozyczenia, DateDiff("d", DataWypozyczenia, DataZwrotu) AS LiczbaDni
FROM Wypozyczenia;
```

**Wynik:**
Zwraca liczbę dni pomiędzy datą wypożyczenia a datą zwrotu.

## Left, Right, Mid

**Składnia:**
```sql
Left(tekst, liczba_znaków)
Right(tekst, liczba_znaków)
Mid(tekst, pozycja_początkowa, [liczba_znaków])
```

**Opis:**
Zwraca fragment tekstu: od lewej strony (`Left`), od prawej strony (`Right`) lub od wybranej pozycji wewnątrz tekstu (`Mid`).

**Przykład:**
```sql
SELECT Pesel
FROM Klienci
WHERE Left(Pesel, 2) = "05";
```

**Wynik:**
Wybiera klientów, których PESEL zaczyna się od „05” (urodzeni w 2005 roku).

## Len

**Składnia:**
```sql
Len(tekst)
```

**Opis:**
Zwraca długość tekstu (liczbę znaków).

**Przykład:**
```sql
SELECT Haslo
FROM Uzytkownicy
WHERE Len(Haslo) < 8;
```

**Wynik:**
Zwraca hasła krótsze niż 8 znaków.

## UCase, LCase

**Składnia:**
```sql
UCase(tekst)
LCase(tekst)
```

**Opis:**
Zamienia litery w tekście na wielkie (`UCase`) lub małe (`LCase`).

**Przykład:**
```sql
SELECT UCase(Nazwisko) AS NazwiskoDuze
FROM Pracownicy;
```

**Wynik:**
Zwraca nazwiska zapisane wielkimi literami.
