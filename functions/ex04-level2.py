def calculate_mean(*lst):
    soma = 0
    media = 0
    for num in lst:
        soma += num
    media = soma / len(lst)
    return media
print('Media: ', calculate_mean(1, 2, 3, 5))