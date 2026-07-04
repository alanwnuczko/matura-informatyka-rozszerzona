def trojkowy(x, k):
    print("0, ")
    y = x
    for i in range(k):
        if y >= 2/3:
            print(2)
        if y < 2/3 and y >= 1/3:
            print(1)
        if y < 1/3:
            print(0)
        y = y * 3
        if y >= 2:
            y = y - 2
        if y >= 1:
            y = y - 1