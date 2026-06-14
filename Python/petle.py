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

for x in range(1, 11): # Liczby od 1 do 10
    print(x) # Drukuje liczby od 1 do 10
