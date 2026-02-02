def contador(inicio, fim, passo):
    if inicio == 1 and fim == 10 and passo == -1:
        for i in range(1, 11):
            print(i, end= " ")
    elif inicio == 10 and fim == 0 and passo == 2:
        for i in range(10, -2, -2):
            print(i, end = ' ')
    else:
        for i in range(ini, fi, pas):
            print(i, end= ' ')



contador(inicio=1, fim=10, passo=-1)
print('')
contador(inicio=10, fim=0, passo=2)
print('')
contador(ini, fi, pas)
ini = int(input('Inicio'))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
#contador(10, 0, 2)
#contador()