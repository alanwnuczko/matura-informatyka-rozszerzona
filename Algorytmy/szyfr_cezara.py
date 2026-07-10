def szyfr_cezara(tekst, przesuniecie):
    wynik = ""

    for znak in tekst:
        if znak.isalpha():
            kod = ord(znak)

            if znak.isupper():
                wynik += chr((kod - 65 + przesuniecie) % 26 + 65)
            else:
                wynik += chr((kod - 97 + przesuniecie) % 26 + 97)

        else:
            wynik += znak
    
    return wynik

def deszyfr_cezara(tekst, przesuniecie):
    return szyfr_cezara(tekst, -przesuniecie)

tekst = input("Podaj tekst: ")
klucz = int(input("Podaj przesunięcie: "))

zaszyfrowany = szyfr_cezara(tekst, klucz)

print("Zaszyfrowany:", zaszyfrowany)
print("Odszyfrowany:", deszyfr_cezara(zaszyfrowany, klucz))