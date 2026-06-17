with open("dane.txt") as f:

    for i in f:
        i = i.strip()

        suma = (1*int(i[0])+3*int(i[1])+7*int(i[2])+9*int(i[3])+1*int(i[4])+3*int(i[5])+7*int(i[6])+9*int(i[7])+1*int(i[8])+3*int(i[9])+int(i[10]))

        if suma % 10 != 0:
            print(i)