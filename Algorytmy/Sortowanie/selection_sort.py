def selection_sort(T):
    n = len(T)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if T[j] < T[min_index]:
                min_index = j

        T[i], T[min_index] = T[min_index], T[i]
    return T

print(selection_sort([4, 2, 7, 11, 3, 2, 9, 1]))