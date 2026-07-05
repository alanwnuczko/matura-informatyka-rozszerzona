liczby_palindromiczne = []
with open("liczby.txt") as f:
    for line in f:
        line = line.strip()
        if line == line[::-1]:
            liczby_palindromiczne.append(line)

for liczba in liczby_palindromiczne:
    print(liczba)