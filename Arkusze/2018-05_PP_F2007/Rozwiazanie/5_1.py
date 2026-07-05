liczby_parzyste = []
with open("liczby.txt") as f:
    for line in f:
        line = int(line.strip())
        if line % 2 == 0:
            liczby_parzyste.append(line)

print(max(liczby_parzyste))