liczby1 = []
liczby2 = []

rowne = 0
wieksze = 0

with open("liczby1.txt") as f:
    for line in f:
        line = int(line.strip(), 8)
        liczby1.append(line)

with open("liczby2.txt") as f:
    for line in f:
        line = int(line.strip())
        liczby2.append(line)

for i in range(0, len(liczby1)):
    if liczby1[i] == liczby2[i]:
        rowne += 1
    elif liczby1[i] > liczby2[i]:
        wieksze += 1

print(f"Równe: {rowne}")
print(f"Liczby1 większe od liczby2: {wieksze}")