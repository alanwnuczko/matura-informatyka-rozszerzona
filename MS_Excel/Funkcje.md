# Funkcje Excel

## SUMA

**Składnia:**
```excel
=FUNKCJA(argument1; argument2)
```

**Opis:**
Dodaje podane liczby lub zakres komórek.

**Przykład:**
```excel
=SUMA(A1:A10)
```

**Wynik:**
Suma wartości z komórek od A1 do A10.

## MIN

**Składnia:**
```excel
=MIN(A1:A10)
```

**Opis:**
Zwraca najmniejszą wartość z podanego zakresu lub listy liczb.

**Przykład:**
```excel
=MIN(C2:C10)
```

**Wynik:**
Najmniejsza wartość z komórek C2:C10.

## MAX

**Składnia:**
```excel
=MAX(A1:A10)
```

**Opis:**
Zwraca największą wartość z podanego zakresu lub listy liczb.

**Przykład:**
```excel
=MAX(C2:C10)
```

**Wynik:**
Największa wartość z komórek C2:C10.

## ŚREDNIA

**Składnia:**
```excel
=ŚREDNIA(A1:A10)
```

**Opis:**
Oblicza średnią arytmetyczną z podanych liczb.

**Przykład:**
```excel
=ŚREDNIA(C2:C10)
```

**Wynik:**
Średnia wartości z komórek C2:C10.

## JEŻELI

**Składnia:**
```excel
=JEŻELI(warunek; wartość_jeżeli_prawda; wartość_jeżeli_fałsz)
```

**Opis:**
Zwraca jedną wartość, gdy warunek jest spełniony, a inną, gdy nie jest.

**Przykład:**
```excel
=JEŻELI(A1>=75;"Zdał";"Nie zdał")
```

**Wynik:**
Wyświetli „Zdał” lub „Nie zdał”.

## LUB

**Składnia:**
```excel
=LUB(warunek1; warunek2)
```

**Opis:**
Zwraca PRAWDA, jeśli przynajmniej jeden warunek jest spełniony.

**Przykład:**
```excel
=LUB(A1>10;B1>10)
```

**Wynik:**
PRAWDA lub FAŁSZ.

## ORAZ

**Składnia:**
```excel
=ORAZ(warunek1; warunek2)
```

**Opis:**
Zwraca PRAWDA tylko wtedy, gdy wszystkie warunki są spełnione.

**Przykład:**
```excel
=ORAZ(A1>10;B1>10)
```

**Wynik:**
PRAWDA lub FAŁSZ.

## LICZ.JEŻELI

**Składnia:**
```excel
=LICZ.JEŻELI(A1:A10;">=50")
```

**Opis:**
Zlicza komórki spełniające podany warunek.

**Przykład:**
```excel
=LICZ.JEŻELI(C2:C10;">=100")
```

**Wynik:**
Liczba komórek o wartości co najmniej 100.

## SUMA.JEŻELI

**Składnia:**
```excel
=SUMA.JEŻELI(A1:A10;">=50";B1:B10)
```

**Opis:**
Sumuje wartości spełniające podany warunek.

**Przykład:**
```excel
=SUMA.JEŻELI(A1:A10;"Kowalski";B1:B10)
```

**Wynik:**
Suma wartości z kolumny B dla wierszy, gdzie w kolumnie A jest „Kowalski”.

## JEŻELI.BŁĄD

**Składnia:**
```excel
=JEŻELI.BŁĄD(A1/B1;0)
```

**Opis:**
Zwraca podaną wartość, jeśli formuła zwróci błąd.

**Przykład:**
```excel
=JEŻELI.BŁĄD(A1/B1;"Błąd")
```

**Wynik:**
Wynik dzielenia lub napis „Błąd”.

## SUMA.WARUNKÓW

**Składnia:**
```excel
=SUMA.WARUNKÓW(C2:C10;A2:A10;">=50";B2:B10;"M")
```

**Opis:**
Sumuje wartości spełniające wiele warunków.

**Przykład:**
```excel
=SUMA.WARUNKÓW(C2:C10;A2:A10;">=18";B2:B10;"Tak")
```

**Wynik:**
Suma wartości z kolumny C dla osób pełnoletnich z wartością „Tak”.

## LICZ.WARUNKI

**Składnia:**
```excel
=LICZ.WARUNKI(A2:A10;">=18";B2:B10;"Tak")
```

**Opis:**
Zlicza komórki spełniające wiele warunków jednocześnie.

**Przykład:**
```excel
=LICZ.WARUNKI(A2:A10;">=50";B2:B10;"M")
```

**Wynik:**
Liczba wierszy spełniających oba warunki.