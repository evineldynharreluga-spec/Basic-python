
def fatorial(number):
    mul = 1
    for i in range(number, 0, -1):
        mul *= i
    print(mul)
fatorial(6)