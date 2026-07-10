# Kody ASCII

## `ord()` (Zamienia znak na liczbę)

Zwraca kod liczbowy dla pojedynczego znaku.

```python
print(ord('A'))   # 65
print(ord('a'))   # 97
print(ord('0'))   # 48
print(ord(' '))   # 32
print(ord('!'))   # 33
```
Działa tylko na string o długości 1.


## `chr()` (Zamienia liczbę na znak)

Odwrotność `ord()`. Zamienia kod liczbowy na znak.

```python
print(chr(65))   # 'A'
print(chr(97))   # 'a'
print(chr(48))   # '0'
print(chr(97 + 1))  # 'b'
```

Działa dla całego zakresu Unicode (0 do 1 114 111)

## Przykłady

- [Zadanie 3.1 (Maj 2026)](Arkusze/2026-05_PR_F2023/Rozwiazanie/3_2.py)
- [Szyfr Cezara](Algorytmy/szyfr_cezara.py)

## Zakresy ASCII

| Zakres | Znaki |
|---|---|
| 0–31 | znaki sterujące (np. 10 = nowa linia, 9 = tabulator) |
| 32 | spacja |
| 48–57 | cyfry '0'-'9' |
| 65–90 | wielkie litery 'A'-'Z' |
| 97–122 | małe litery 'a'-'z' |

## Stałe ASCII z modułu `string`
```python
import string
print(string.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)           # 0123456789
```