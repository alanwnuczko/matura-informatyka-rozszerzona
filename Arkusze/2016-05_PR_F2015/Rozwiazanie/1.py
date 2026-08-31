def dzielniki(n):
    dzielniki = []
    for i in range(1, n):
        if n % i == 0:
            dzielniki.append(i)
    return dzielniki

print(dzielniki(75)) # Dzielniki a (mniejsze od a)
print(dzielniki(48)) # Dzielniki b (mniejsze od b)

print(sum(dzielniki(75))) # Suma dzielników a
print(sum(dzielniki(48))) # Suma dzielników b