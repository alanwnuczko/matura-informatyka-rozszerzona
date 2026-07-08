wszystkie_liczby = []
with open("liczby1.txt") as f:
    for line in f:
        wszystkie_liczby.append(int(line, 8))

max_liczba = max(wszystkie_liczby)
min_liczba = min(wszystkie_liczby)

max_liczba_oct = oct(max_liczba)[2:]
min_liczba_oct = oct(min_liczba)[2:]

print(f"Największa liczba: {max_liczba_oct}")
print(f"Najmniejsza liczba: {min_liczba_oct}")