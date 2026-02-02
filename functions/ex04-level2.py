def calculate_mean(*lst):
    soma = 0
    media = 0
    for num in lst:
        soma += num
    media = soma / len(lst)
    return media
print('Media: ', calculate_mean(1, 2, 3, 5))

def calculate_median(*lst):
    tamanho = int(len(lst) / 2)
    if len(lst)-1 % 2 == 0:
        elemento = lst[tamanho]
        print('Mediana e: ',elemento)
    else:
        elemento_1 = lst[tamanho-1]
        elemento_2 = lst[tamanho]
        mediana = (elemento_2 + elemento_1)/2
        print('Mediana e ',mediana)
print(calculate_median(1, 3, 5, 7, 9, 11, 13))