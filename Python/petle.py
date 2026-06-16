x = 3
y = 7
z = 9

# Pętla if
if x > y:
    print("x jest większe od y")
elif x == 0:
    print("x jest równe 0")
else:
    print("x jest mniejsze od y")

if y > x and z > x:
    print("Oba warunki zostały spełnione")

# Pętla while
i = 0
while i <= 10:
    print(i)
    i += 1

# Pętla for
owoce = ["pomarańcza", "jabłko", "kiwi"]
for x in owoce:
    print(x) # Wyświetla każdy element listy osobno

for x in "Winogrona":
    print(x) # Wyświetla każdą litere ze słowa winogrona

for x in range(1, 11):
    print(x)

for x in range(1, 11, 2): # Od 1 do 10 co 2 (nieparzyste)
    print(x)

# in - sprawdza czy wartość jest obecna
lista = [3, 4, 7, 1 , 2, 9, 8]
wyszukiwana_liczba = 5

if wyszukiwana_liczba in lista: # Czy wyszukiwana lista jest w liście
    print(f"{wyszukiwana_liczba} znajduje się w liście")
else:
    print(f"{wyszukiwana_liczba} nie znajduje się w liście")
