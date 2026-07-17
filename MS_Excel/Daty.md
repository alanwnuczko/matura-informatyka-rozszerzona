# Daty

## DATA

**Składnia:**
```excel
=DATA(rok;miesiąc;dzień)
```

**Opis:**
Tworzy datę z podanych wartości roku, miesiąca i dnia.

**Przykład:**
```excel
=DATA(2026;7;9)
```

**Wynik:**
09.07.2026

## DZIEŃ.TYGODNIA

**Składnia:**
```excel
=DZIEŃ.TYGODNIA(data;[typ])
```

**Opis:**
Zwraca numer dnia tygodnia dla podanej daty.

**Parametr `[typ]`:**
- `1` lub pominięty - 1 = niedziela, ..., 7 = sobota
- `2` - 1 = poniedziałek, ..., 7 = niedziela
- `3` - 0 = poniedziałek, ..., 6 = niedziela

**Przykład:**
```excel
=DZIEŃ.TYGODNIA(A1;2)
```

**Wynik:**
Liczba od 1 do 7, gdzie:
- 1 - poniedziałek
- 7 - niedziela

## ROK

**Składnia:**
```excel
=ROK(A1)
```

**Opis:**
Zwraca rok z podanej daty.

**Przykład:**
```excel
=ROK(A1)
```

**Wynik:**
Np. 2026.

## MIESIĄC

**Składnia:**
```excel
=MIESIĄC(A1)
```

**Opis:**
Zwraca numer miesiąca z podanej daty.

**Przykład:**
```excel
=MIESIĄC(A1)
```

**Wynik:**
Np. 7.

## DZIEŃ

**Składnia:**
```excel
=DZIEŃ(A1)
```

**Opis:**
Zwraca dzień miesiąca z podanej daty.

**Przykład:**
```excel
=DZIEŃ(A1)
```

**Wynik:**
Np. 9.

## DNI.ROBOCZE

**Składnia:**
```excel
=DNI.ROBOCZE(data_początkowa;data_końcowa)
```

**Opis:**
Zwraca liczbę dni roboczych między dwiema datami (bez sobót i niedziel).

**Przykład:**
```excel
=DNI.ROBOCZE(A1;B1)
```

**Wynik:**
Liczba dni roboczych między datami z A1 i B1.

## TERAZ

**Składnia:**
```excel
=TERAZ()
```

**Opis:**
Zwraca aktualną datę i godzinę.

**Przykład:**
```excel
=TERAZ()
```

**Wynik:**
Aktualna data i czas.

## GODZINA

**Składnia:**
```excel
=GODZINA(A1)
```

**Opis:**
Zwraca godzinę z podanej daty lub czasu.

**Przykład:**
```excel
=GODZINA(A1)
```

**Wynik:**
Np. 14.

## MINUTA

**Składnia:**
```excel
=MINUTA(A1)
```

**Opis:**
Zwraca minuty z podanej daty lub czasu.

**Przykład:**
```excel
=MINUTA(A1)
```

**Wynik:**
Np. 30.

## SEKUNDA

**Składnia:**
```excel
=SEKUNDA(A1)
```

**Opis:**
Zwraca sekundy z podanej daty lub czasu.

**Przykład:**
```excel
=SEKUNDA(A1)
```

**Wynik:**
Np. 45.