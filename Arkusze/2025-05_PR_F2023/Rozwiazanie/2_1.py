with open("symbole.txt") as f:
    for line in f:
        line = line.strip()
        if line == line[::-1]:
            print(line)