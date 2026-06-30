def J(n):
     i = 1
     while n > 0:
         if n% 2 == 1:
             print(i)
         n = n // 2
         i += 1

print(J(75))