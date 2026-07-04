def binarny(x, k):
    print("0,")
    y = x
    for i in range(1, k+1):
        print(y)
        if y >= 1/2:
            print(1)
        else:
            print(0)
        y = y * 2
        if y >= 1:
            y = y - 1

print(binarny(0.6, 5))