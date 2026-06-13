# Operatory arytmetyczne
x = 7
y = 3

dodawanie = x + y
print(dodawanie)

odejmowanie = x - y
print(odejmowanie)

mnozenie = x * y
print(mnozenie)

dzielenie = x / y
print(dzielenie)

modulo = x % y # Zwraca resztę z dzielenia
print(modulo)

potega = x ** y
print(potega)

floor = x // y # Dzielenie podłogowe - 2.3333333333333335 zaokrągla w dół - zwraca 2
print(floor)


# Operatory przypisania

x += 3 # x = x + 3
x -= 3 # x = x - 3
x *= 3 # x = x * 3
x /= 3 # x = x / 3
x %= 3 # x = x % 3
x //= 3 # x = x // 3
x **= 3 # x = x ** 3


# Operatory porównania

x = 7
y = 3
z = 3

x == y # False
x != y # True
x >  y # True
x < y # False
x >= y # True
y >= z # True
x <= y # False


# Operatory logiczne

print(x > 0 and y == 3 ) # Oba warunki zostały spełnione (&&)
print(x < 0 or y < 0) # Jeden z warunków został spełniony (||)