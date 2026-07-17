A = 0
B = 0

with open("mecz.txt") as f:
    wyniki = f.readline().strip()
    wyniki = list(wyniki)

    for wynik in wyniki:
        if wynik == "A":
            A += 1
        else:
            B += 1

        if A >= 1000 and B <= A - 3:
            print("A", A, ":", B)
            break

        if B >= 1000 and A <= B - 3:
            print("B", A, ":", B)
            break