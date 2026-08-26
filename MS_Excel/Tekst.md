# Funkcje tekstowe

## LEWY

**Składnia:**
```excel
=LEWY(tekst; [liczba_znaków])
```

**Opis:**
Zwraca określoną liczbę znaków od początku tekstu (od lewej strony). Jeśli parametr `[liczba_znaków]` zostanie pominięty, zwraca 1 znak.

**Przykład:**
```excel
=LEWY(A1; 2)
```

**Wynik:**
Dla tekstu „Warszawa” w A1 wynikiem jest „Wa”.

## PRAWY

**Składnia:**
```excel
=PRAWY(tekst; [liczba_znaków])
```

**Opis:**
Zwraca określoną liczbę znaków od końca tekstu (od prawej strony). Jeśli parametr `[liczba_znaków]` zostanie pominięty, zwraca 1 znak.

**Przykład:**
```excel
=PRAWY(A1; 3)
```

**Wynik:**
Dla tekstu „Warszawa” w A1 wynikiem jest „awa”.

## FRAGMENT.TEKSTU

**Składnia:**
```excel
=FRAGMENT.TEKSTU(tekst; liczba_początkowa; liczba_znaków)
```

**Opis:**
Zwraca określoną liczbę znaków z tekstu, zaczynając od wskazanej pozycji.

**Przykład:**
```excel
=FRAGMENT.TEKSTU(A1; 3; 4)
```

**Wynik:**
Dla tekstu „Warszawa” w A1 wynikiem jest „rsza”.

## DŁ

**Składnia:**
```excel
=DŁ(tekst)
```

**Opis:**
Zwraca liczbę znaków w podanym tekście (wliczając spacje i znaki specjalne).

**Przykład:**
```excel
=DŁ(A1)
```

**Wynik:**
Dla tekstu „Informatyka” w A1 wynikiem jest 11.

## ZŁĄCZ.TEKST / &

**Składnia:**
```excel
=ZŁĄCZ.TEKST(tekst1; [tekst2]; ...)
```
Z operatorem `&`:
```excel
=tekst1 & tekst2
```

**Opis:**
Łączy dwa lub więcej ciągów tekstowych w jeden.

**Przykład:**
```excel
=A1 & " " & B1
```

**Wynik:**
Dla A1 = „Jan” i B1 = „Kowalski” wynikiem jest „Jan Kowalski”.

## ZNAJDŹ

**Składnia:**
```excel
=ZNAJDŹ(szukany_tekst; w_tekście; [liczba_początkowa])
```

**Opis:**
Zwraca pozycję początkową danego ciągu tekstowego wewnątrz innego tekstu (rozróżnia wielkość liter).

**Przykład:**
```excel
=ZNAJDŹ("@"; A1)
```

**Wynik:**
Dla tekstu „jan.kowalski@gmail.com” w A1 wynikiem jest 13.

## PODSTAW

**Składnia:**
```excel
=PODSTAW(tekst; stary_tekst; nowy_tekst; [które_wystąpienie])
```

**Opis:**
Zastępuje istniejący tekst nowym tekstem w podanym ciągu.

**Przykład:**
```excel
=PODSTAW(A1; ","; ".")
```

**Wynik:**
Dla tekstu „12,50” w A1 wynikiem jest „12.50”.

## WARTOŚĆ

**Składnia:**
```excel
=WARTOŚĆ(tekst)
```

**Opis:**
Konwertuje ciąg tekstowy reprezentujący liczbę na rzeczywistą wartość liczbową (niezbędne, gdy liczby zaimportowane z pliku są traktowane przez Excel jako tekst).

**Przykład:**
```excel
=WARTOŚĆ(A1)
```

**Wynik:**
Dla tekstu „123” w A1 wynikiem jest liczba 123.

## LITERY.WIELKIE

**Składnia:**
```excel
=LITERY.WIELKIE(tekst)
```

**Opis:**
Zamienia wszystkie litery w tekście na wielkie (duże).

**Przykład:**
```excel
=LITERY.WIELKIE(A1)
```

**Wynik:**
Dla tekstu „matura” w A1 wynikiem jest „MATURA”.

## LITERY.MAŁE

**Składnia:**
```excel
=LITERY.MAŁE(tekst)
```

**Opis:**
Zamienia wszystkie litery w tekście na małe.

**Przykład:**
```excel
=LITERY.MAŁE(A1)
```

**Wynik:**
Dla tekstu „MATURA” w A1 wynikiem jest „matura”.

## USUŃ.ZBĘDNE.ODSTĘPY

**Składnia:**
```excel
=USUŃ.ZBĘDNE.ODSTĘPY(tekst)
```

**Opis:**
Usuwa wszystkie spacje wiodące i końcowe z tekstu oraz zastępuje wielokrotne spacje wewnątrz tekstu pojedynczą spacją.

**Przykład:**
```excel
=USUŃ.ZBĘDNE.ODSTĘPY("  Jan   Kowalski  ")
```

**Wynik:**
„Jan Kowalski”.
