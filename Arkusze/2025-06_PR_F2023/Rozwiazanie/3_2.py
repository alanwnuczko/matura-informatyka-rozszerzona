with open("dane.txt") as f:
    napis = f.read()
    cyfry = [0] * 10

    for znak in napis:
        if znak.isdigit():
            cyfry[int(znak)] += 1

indeks_najczestszej_cyfry = cyfry.index(max(cyfry))
print(indeks_najczestszej_cyfry) # Cyfra występująca najczęsciej
print(max(cyfry)) # Liczba wystąpień najczęściej występującej cyfry