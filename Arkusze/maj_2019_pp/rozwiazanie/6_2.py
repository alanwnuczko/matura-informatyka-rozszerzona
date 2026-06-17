with open("dane.txt") as f:
    liczba_osob_listopad = 0
    for i in f:
        miesiac = i[2]+i[3]
        if miesiac == "11" or miesiac == "31":
            liczba_osob_listopad += 1
print(liczba_osob_listopad)