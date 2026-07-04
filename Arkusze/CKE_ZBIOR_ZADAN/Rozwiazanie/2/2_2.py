def binarny(x, k):
    print("0,")
    y = x
    for i in range(k+1):
        if y >= 1/2:
            print(1)
        else:
            print(0)
        y = y * 2
        if y >= 1:
            y = y - 1
    print(y)

print(binarny(1/16, 4))
print(binarny(1/16, 3))

# Odpowiedź: 1/16 (0.0625)