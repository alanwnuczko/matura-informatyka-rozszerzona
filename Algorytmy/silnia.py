def silnia(n):
    if n < 0:
        raise ValueError("n nie może być ujemne.")
    elif n == 1 or n == 0:
        return 1
        
    wynik = 1
    for i in range(1, n+1):
           wynik *= i
    return wynik
    
print(silnia(3)) # Wynik: 6 (3! = 3 * 2 * 1 = 6)