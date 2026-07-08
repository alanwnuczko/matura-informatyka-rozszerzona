with open("liczby.txt") as f:
    for line in f:
        liczba = int(line.strip())

        dzielniki = []

        for i in range(1, liczba + 1):
            if liczba % i == 0:
                dzielniki.append(i)

        dzielniki.sort()

        if len(dzielniki) == 18:
            print(liczba, dzielniki)