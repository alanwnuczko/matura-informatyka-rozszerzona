def algorytm(W):
    W[0] = 1
    W[1] = 1
    W[2] = 1
    max_wart = 1
    for i in range(3, 10001):
        if i % 2 == 0:
            W[i] = W[i - 3] + W[i - 1] + 1
        else:
            W[i] = W[i - 1] % 7
        if W[i] > max_wart:
            W[i] = max_wart
    return max_wart

# Pseudokod:

# W[0] ← 1
# W[1] ← 1
# W[2] ← 1
# max_wart ← 1
# dla i = 3, 4, …, 1 000 wykonuj
#   jeżeli i mod 2 = 0
#       W[i] ← W[i - 1] + W[i - 1] + 1
#   w przeciwnym razie
#       W[i] ← W[i - 1] mod 7
#   jeżeli W[i] > max_wart
#       W[i] = max_wart
# zwróć max_wart
