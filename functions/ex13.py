def sum_of_numbers(number):
    soma = 0
    somatorio = []
    for i in range(0, number+1):
        soma += i
    return soma
print(sum_of_numbers(100))