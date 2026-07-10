def prefiksosufiks(s1, s2):
    maks = 0

    for i in range(1, len(s1) + 1):
        if s2.endswith(s1[:i]):
            maks = i

    for i in range(1, len(s2) + 1):
        if s1.endswith(s2[:i]):
            maks = max(maks, i)

    return maks


with open("pary.txt") as file:
    for line in file:
        s1, s2 = line.split()

        wynik = prefiksosufiks(s1, s2)

        if wynik >= 5:
            print(s1, s2, wynik)