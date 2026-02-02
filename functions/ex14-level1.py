def sum_of_odds(number):
    soma_impar = 0
    for i in range(0, number+1):
        if i % 2 != 0:
            soma_impar += i
    return soma_impar

print(sum_of_odds(9))