# Symulacja

## LOS

**Składnia:**
```excel
=LOS()
```

**Opis:**
Zwraca losową liczbę rzeczywistą z przedziału od 0 (włącznie) do 1 (bez 1). Wartość zmienia się przy każdym przeliczeniu arkusza (F9).

**Przykład:**
```excel
=LOS()
```

**Wynik:**
Np. 0,374821 (losowa wartość z zakresu [0; 1)).

## LOS.ZAKR

**Składnia:**
```excel
=LOS.ZAKR(dolna; górna)
```

**Opis:**
Zwraca losową liczbę całkowitą z podanego przedziału (oba końce włącznie).

**Przykład:**
```excel
=LOS.ZAKR(1; 6)
```

**Wynik:**
Losowa liczba całkowita od 1 do 6 (symulacja rzutu kostką).

## RESZTA

**Składnia:**
```excel
=MOD(liczba; dzielnik)
```

**Opis:**
Zwraca resztę z dzielenia (modulo). Do wykrywania parzystości, cykliczności i powtarzalnych wzorców.

**Przykład:**
```excel
=MOD(A1; 2)
```

**Wynik:**
0 dla liczb parzystych, 1 dla nieparzystych.

## ZAOKR

**Składnia:**
```excel
=ZAOKR(liczba; liczba_cyfr)
```

**Opis:**
Zaokrągla liczbę do podanej liczby miejsc po przecinku.

**Przykład:**
```excel
=ZAOKR(A1*0,07; 2)
```

**Wynik:**
Zaokrąglony wynik do 2 miejsc po przecinku (np. obliczanie odsetek).

## ZAOKR.DO.CAŁK

**Składnia:**
```excel
=ZAOKR.DO.CAŁK(liczba)
```

**Opis:**
Zaokrągla liczbę w dół do najbliższej liczby całkowitej.

**Przykład:**
```excel
=ZAOKR.DO.CAŁK(LOS()*10)
```

**Wynik:**
Losowa liczba całkowita od 0 do 9.

## Symulacja z warunkiem (JEŻELI + LOSOWO)

**Składnia:**
```excel
=JEŻELI(LOS() < prawdopodobieństwo; wynik_sukcesu; wynik_porażki)
```

**Opis:**
Symuluje zdarzenie losowe o danym prawdopodobieństwie. Jeśli wylosowana wartość jest mniejsza od zadanego progu, zdarzenie zachodzi.

**Przykład:**
```excel
=JEŻELI(LOS() < 0,3; "Deszcz"; "Słonecznie")
```

**Wynik:**
Z prawdopodobieństwem 30% zwraca "Deszcz", w przeciwnym razie "Słonecznie".

## Symulacja krokowa (odwołanie do poprzedniego wiersza)

**Składnia:**
```excel
=B1 + zmiana
```

**Opis:**
Każdy wiersz arkusza reprezentuje jeden krok symulacji. Wartość w bieżącym wierszu zależy od wartości w wierszu poprzednim. Pierwszy wiersz zawiera wartość początkową.

**Przykład:**
```excel
Wiersz 1 (wartość początkowa):  =1000
Wiersz 2:                       =B1 * 1,05
Wiersz 3:                       =B2 * 1,05
```

**Wynik:**
Symulacja wzrostu o 5% w każdym kroku (np. oprocentowanie lokaty): 1000, 1050, 1102,50...

## Zliczanie wyników symulacji (LICZ.JEŻELI)

**Składnia:**
```excel
=LICZ.JEŻELI(zakres; kryterium)
```

**Opis:**
Po przeprowadzeniu symulacji w kolumnie, zlicza ile razy wystąpił dany wynik. Pozwala oszacować prawdopodobieństwo na podstawie wielu prób.

**Przykład:**
```excel
=LICZ.JEŻELI(A1:A1000; "Deszcz") / 1000
```

**Wynik:**
Udział procentowy wystąpień "Deszcz" w 1000 próbach (oszacowanie prawdopodobieństwa).
