wszystkie_liczby = []
with open("liczby2.txt") as f:
    for line in f:
        wszystkie_liczby.append(int(line.strip()))

najdluzszy = 1
poczatek = wszystkie_liczby[0]

aktualny = 1
start = wszystkie_liczby[0]

for i in range(1, len(wszystkie_liczby)):
    if wszystkie_liczby[i] >= wszystkie_liczby[i - 1]:
        aktualny += 1
    else:
        if aktualny > najdluzszy:
            najdluzszy = aktualny
            poczatek = start

        aktualny = 1
        start = wszystkie_liczby[i]

if aktualny > najdluzszy:
    najdluzszy = aktualny
    poczatek = start

print(poczatek, najdluzszy)