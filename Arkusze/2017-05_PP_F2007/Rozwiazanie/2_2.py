def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def czy_blizniacza(a):
    if a < 3:
        print("NIE")
        return
    if czy_pierwsza(a) == False:
        print("NIE")
    else:
        if czy_pierwsza(a-2) or czy_pierwsza(a+2):
            print("TAK")
        else:
            print("NIE")

print(czy_blizniacza(5))