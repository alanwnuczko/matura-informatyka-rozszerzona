with open("dane.txt") as f:
    kobiet = 0
    mezczyzn = 0
    for i in f:
        i = i.strip()
        if int(i[9]) % 2 == 0:
            kobiet += 1
        else:
            mezczyzn += 1
print(f"Kobiet: {kobiet}, mężczyzn: {mezczyzn}")