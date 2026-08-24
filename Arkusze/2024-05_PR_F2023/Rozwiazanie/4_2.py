with open("liczby.txt") as f:
    pierwsza_linia = list(map(int, f.readline().split()))

    pierwsza_linia.sort(reverse=True)
    print(pierwsza_linia[100])