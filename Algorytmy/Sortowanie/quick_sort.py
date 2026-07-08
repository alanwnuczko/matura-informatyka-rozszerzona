def quick_sort(T):
    if len(T) <= 1:
        return T
    pivot = T[len(T) // 2]

    left = []
    center = []
    right = []

    for x in T:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            center.append(x)
        else:
            right.append(x)

    return quick_sort(left) + center + quick_sort(right)
print(quick_sort([4, 2, 7, 11, 3, 2, 9, 1]))