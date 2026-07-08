liczby_dziesietnie = []
liczby_osemkowo = []
with open("liczby2.txt") as f:
    for line in f:
        liczby_dziesietnie.append(line.strip())
        liczba_8 = int(line.strip())
        liczba_8 = oct(liczba_8)
        liczby_osemkowo.append(liczba_8[2:])

# print(liczby_dziesietnie)
# print(liczby_osemkowo)

szostki_w_dziesietnych = 0
szostki_w_osemkowych = 0

for liczba in liczby_dziesietnie:
    szostki_w_dziesietnych += liczba.count("6")

for liczba in liczby_osemkowo:
    szostki_w_osemkowych += liczba.count("6")

print(f"Szóstki w dziesiętnych: {szostki_w_dziesietnych}")
print(f"Szóstki w ósemkowych: {szostki_w_osemkowych}")