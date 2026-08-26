# Funkcje wyszukiwania

## WYSZUKAJ.PIONOWO

**Składnia:**
```excel
=WYSZUKAJ.PIONOWO(szukana_wartość; tabela_tablica; nr_indeksu_kolumny; [zakres_wyszukiwania])
```

**Opis:**
Przeszukuje pierwszą (skrajnie lewą) kolumnę zakresu w poszukiwaniu podanej wartości i zwraca wartość z tej samej linii z określonej kolumny.

**Parametr `[zakres_wyszukiwania]`:**
- `FAŁSZ` lub `0` - dokładne dopasowanie
- `PRAWDA` lub `1` - dopasowanie przybliżone (wymaga posortowania pierwszej kolumny)

**Przykład:**
```excel
=WYSZUKAJ.PIONOWO(A2; $D$2:$F$100; 3; FAŁSZ)
```

**Wynik:**
Zwraca wartość z 3. kolumny tabeli `$D$2:$F$100` odpowiadającą kluczowi z komórki `A2`.

## PODAJ.POZYCJĘ

**Składnia:**
```excel
=PODAJ.POZYCJĘ(szukana_wartość; przeszukiwana_tablica; [typ_porównania])
```

**Opis:**
Zwraca względną pozycję (indeks) szukanej wartości w jednowymiarowym wierszu lub kolumnie.

**Parametr `[typ_porównania]`:**
- `0` - dokładne dopasowanie
- `1` - największa wartość mniejsza lub równa szukanej (wymaga sortowania rosnącego)
- `-1` - najmniejsza wartość większa lub równa szukanej (wymaga sortowania malejącego)

**Przykład:**
```excel
=PODAJ.POZYCJĘ(A1; C1:C10; 0)
```

**Wynik:**
Numer wiersza w zakresie `C1:C10`, w którym znajduje się wartość z `A1` (np. `4`).

## INDEKS

**Składnia:**
```excel
=INDEKS(tablica; nr_wiersza; [nr_kolumny])
```

**Opis:**
Zwraca wartość komórki znajdującej się na przecięciu podanego numeru wiersza i kolumny w danym zakresie.

**Przykład:**
```excel
=INDEKS(B2:B10; 3)
```

**Wynik:**
Wartość z 3. wiersza zakresu `B2:B10`.

## INDEKS + PODAJ.POZYCJĘ

**Składnia:**
```excel
=INDEKS(kolumna_wynikowa; PODAJ.POZYCJĘ(szukana_wartość; kolumna_klucza; 0))
```

**Opis:**
Połączenie dwóch funkcji działające jak elastyczny odpowiednik `WYSZUKAJ.PIONOWO` - pozwala wyszukiwać wartości na lewo od kolumny klucza oraz nie zależy od stałych indeksów kolumn.

**Przykład:**
```excel
=INDEKS($A$2:$A$100; PODAJ.POZYCJĘ(E2; $B$2:$B$100; 0))
```

**Wynik:**
Zwraca wartość z kolumny A dla wiersza, w którym w kolumnie B znaleziono wartość `E2`.
