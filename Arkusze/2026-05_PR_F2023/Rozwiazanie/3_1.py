def f(s):
    wartosci_ascii = []
    for letter in s:
        wartosci_ascii.append(ord(letter))
    return sum(wartosci_ascii)

# print(abs(f("oko") - f("pies")))

pary_slow = []
wartosci_bezwzgledne = []
with open("pary.txt") as file:
    for line in file:
        line = line.split()
        pary_slow.append(line)
        wartosci_bezwzgledne.append(abs(f(line[0]) - f(line[1])))

# print(pary_slow)
# print(max(wartosci_bezwzgledne))

maks = max(wartosci_bezwzgledne)
for i in range(len(wartosci_bezwzgledne)):
    if wartosci_bezwzgledne[i] == maks:
        print(pary_slow[i][0], pary_slow[i][1], maks)
