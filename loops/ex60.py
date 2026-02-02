5 * 4 * 3 * 2 * 1
num = int(input('Numero: '))

mul = 1
for i in range(num, 0, -1):
    mul *= i
    #print(i, end= "")
    print(i, end= " x ",)
print(mul)