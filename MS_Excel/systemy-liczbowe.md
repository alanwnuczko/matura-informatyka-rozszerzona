# Systemy liczbowe

## Zamiana z innego systemu na dziesiętny

**Konsola Python:**
```python
int("1101", 2)
13

int("101", 8)
65

int("E9", 16)
233

int("1021", 3)
34
```

**Excel:**
```
=DZIESIĘTNA("1021"; 3)
34

=DZIESIĘTNA("E9"; 16)
233
```

> `int(liczba, podstawa)` i `=DZIESIĘTNA()` działają dla podstaw od 2 do 36.

## Zamiana liczby dziesiętnej na inny system

### Dwójkowy, ósemkowy, szesnastkowy

**Konsola Python:**
```python
bin(65)
'0b1000001'

bin(65)[2:]  # usuwa prefiks '0b'
'1000001'

oct(65)
'0o101'

oct(65)[2:]  # usuwa prefiks '0o'
'101'

hex(65)
'0x41'

hex(65)[2:]  # usuwa prefiks '0x'
'41'
```

**Excel:**
```
=DZIES.NA.DWÓJK(65)
1000001

=DZIES.NA.ÓSM(65)
101

=DZIES.NA.SZESN(65)
41
```

### Pozostałe (dowolna podstawa)

**Excel:**
```
=PODSTAWA(34; 3)
1021
```

**Python nie ma wbudowanej funkcji**
