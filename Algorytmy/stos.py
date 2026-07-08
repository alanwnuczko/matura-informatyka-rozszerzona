stos = []

# Push() - Dodaje element na szczyt stosu
for i in range(7):
    stos.append(i)
print(stos)

# Pop()
stos.pop() # Usuwa element ze szczytu stosu
print(stos)

# Peek()
print(stos[-1]) # Zwraca element ze szczytu stosu

# isEmpty() - zwraca czy stos jest pusty
if stos:
    print(False)
else:
    print(True)

# size() - zwraca ilość elementów stosu
print(len(stos))