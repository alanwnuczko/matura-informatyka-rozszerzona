f = open("liczby.txt")

ile = 0

for i in f:
    liczba = int(i)
    while liczba % 3 == 0:
        liczba //= 3

    if liczba == 1:
        ile += 1

print(ile)

f.close()