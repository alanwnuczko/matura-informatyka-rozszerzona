# abs() - zwraca wartość bezwzględną liczby
abs(-5)  # wynik: 5
abs(3)   # wynik: 3
abs(-2.5) # wynik: 2.5


# round() - zaokrągla liczbę do najbliższej liczby całkowitej
round(3.2)  # wynik: 3
round(3.7)  # wynik: 4
round(3.5)  # wynik: 4 (zaokrągla w górę)
round(3.14159, 2)  # wynik: 3.14 (zaokrągla do 2 miejsc po przecinku)


# pow() - podnosi liczbę do potęgi
pow(2, 5)  # wynik: 32 (2 do potęgi 5)
pow(3, 3)  # wynik: 27 (3 do potęgi 3)


# divmod() - zwraca wynik dzielenia i resztę z dzielenia jako krotkę
divmod(7, 3)  # wynik: (2, 1) - 2 to wynik dzielenia, 1 to reszta
divmod(10, 4) # wynik: (2, 2) - 2 to wynik dzielenia, 2 to reszta


# bin(), hex(), oct()
bin(2) # Wynik: 0b10 - 2 binarnie to 10
print(bin(2)[2:]) # Wynik: 10  - bez 0b na początku

hex(255) # Wynik: 0xff - 255 szesnastkowo to FF
print(hex(255)[2:]) # Wynik: ff - bez 0x na początku

oct(16) # Wynik: 0o20 - 16 Ósemkowo to 20
print(oct(16)[2:]) # Wynik: 20 - bez 0o na początku


# int(a) - zamiana stringa na int
int("1212") # Wynik: 1212

# int("a", podstawa) - zamiana z systemu liczbowego na dziesiętny
int("1212", 5) # Wynik: 182
int("102", 3) # Wynik: 11
int("F1", 16) # Wynik: 241


# import math (biblioteka math)
import math

# math.sqrt() - pierwiastek
print(math.sqrt(16))

# math.ceil() - zaokrąglenie w góre
print(math.ceil(3.1)) # 4

# math.floor() - zaokrąglenie w dół
print(math.floor(5.7)) # 5

# math.gcd() - Greatest Common Divisor - Największy wspólny dzielnik NWD
print(math.gcd(5, 25)) # 5
print(math.gcd(45, 81)) # 9

# math.lcm() - Least Common Multiple - Najmniejsza wspólna wielokrotność NWW
print(math.lcm(3, 8)) # 24


# .strip(), .lstrip(), .rstrip() - usuwanie białych znaków
importowane = "   Python  "
print(importowane.strip())  # Usuwa białe znaki z obu stron: "Python"
print(importowane.lstrip()) # Usuwa białe znaki z lewej strony: "Python  "
print(importowane.rstrip()) # Usuwa białe znaki z prawej strony: "   Python"


# str.split() - dzieli string na listę słów
string = "Byłem w sklepie"
print(string.split()) # Wynik: ['Byłem', 'w', 'sklepie']

csv = "10,1101,1011"
print(csv.split(",")) # Wynik: ['10', '1101', '1011']


# .join() łączy elementy listy w słowo
lista = ["P", "y", "t", "h", "o", "n"]
print("".join(lista)) # Wynik: Python


# .lower(), .upper() - zamieniają znaki w stringu na małe lub wielkie litery
str = "TeKSt"
print(str.lower()) # Wynik: tekst
print(str.upper()) # Wynik: TEKST


# .isdigit() - sprawdza czy w stringu są same cyfry
# .isalpha() - sprawdza czy w stringu są same litery


# max(lista) - zwraca największą wartość z listy
# min(lista) - zwraca najmniejszą wartość z listy
# len(lista) - zwraca ilość elementów w liście
# sum(lista) - zwraca sumę elementów w liście
# sorted(lista) - zwraca posortowaną listę
# sorted(lista, reverse=True) - zwraca listę posortowaną malejąco
