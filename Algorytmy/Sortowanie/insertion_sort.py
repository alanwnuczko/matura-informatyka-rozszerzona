def insertion_sort(T):
    n = len(T)

    for i in range(1, n):
        x = T[i]
        j = i - 1

        while j >= 0 and T[j] > x:
            T[j + 1] = T[j]
            j -= 1

        T[j + 1] = x

    return T

print(insertion_sort([4, 2, 7, 11, 3, 2, 9, 1]))
