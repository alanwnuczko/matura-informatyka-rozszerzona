# k = cena biletów (cena w systemie pozycyjnym)
# p = podstawa
def algorytm(k, p):
    k_dziesietnie = int(str(k), p)
    wynik = oct(k_dziesietnie)
    return wynik[2:]

print(algorytm(2210, 3))