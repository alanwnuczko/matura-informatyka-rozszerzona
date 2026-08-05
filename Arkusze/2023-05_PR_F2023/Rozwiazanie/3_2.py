cyfry = []
with open("pi.txt") as f:
    for line in f:
        cyfry.append(line.strip())

zliczenia = [0] * 100

for i in range(len(cyfry) - 1):
    fragment = int(cyfry[i] + cyfry[i+1])
    zliczenia[fragment] += 1

min_wystapienia = min(zliczenia)
max_wystapienia = max(zliczenia)

min_fragment = zliczenia.index(min_wystapienia)
max_fragment = zliczenia.index(max_wystapienia)

print(min_fragment, min_wystapienia)
print(max_fragment, max_wystapienia)