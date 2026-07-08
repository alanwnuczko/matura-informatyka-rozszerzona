kolejka = []

# enqueue() - dodaje element na koniec kolejki
kolejka.append(2)
kolejka.append(4)
kolejka.append(6)
kolejka.append(8)
kolejka.append(10)
print(kolejka)

# dequeue() - usuwa element z przodu kolejki
kolejka.pop(0)
kolejka.pop(0)
print(kolejka)

# peek() - zwraca element z przodu kolejki
print(kolejka[0])

# isEmpty() - zwraca czy kolejka jest pusta
if kolejka:
    print(False)
else:
    print(True)

# size() - zwraca ilość elementów w kolejce
print(len(kolejka))