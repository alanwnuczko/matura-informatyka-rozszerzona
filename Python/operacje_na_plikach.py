f = open("1.txt") # Otwiera plik przyklad.txt
print(f.read()) # Wyświetla wczytany plik
f.close() # Zamyka plik

with open("1.txt") as f: # Otwiera plik i przypisuje zawartośc do zmiennej f
    print(f.read()) # Wyświetla wczytany plik
    print(f.read(10)) # Wyświetla pierwsze 10 znaków pliku

with open("przyklad.txt") as f:
    print(f.readline()) # Wyświetla pierwszą linię pliku

with open("1.txt") as f:
    for i in f: # Pętla po każdej linijce pliku
        print(i)

with open("1.txt") as f:
    for i in f:
        print(int(i) ** 2) # Zamienia string na int i wyświetla liczbę do potęgi 2 dla każdej linijki pliku

with open("1.txt", "a") as f: # "a" dodaje tekst na koniec pliku
    f.write(" Koniec pliku")
    print(f.read())

with open("1.txt", "w") as f:
    f.write("Zamienia zawartość pliku na ten tekst")

f = open("nowy_plik.txt", "x") # "x" tworzy nowy plik, jeśli już istnieje to zwróci błąd