''''3456
Unidade : 6
Dezena  : 5
Centena : 4
Milhar : 3'''

numero = str(input('Introduza um numero de 0 a 9999: '))
#nr_stripped = numero.split()
tamanho = len(numero)
if tamanho == 1:
    print(f'Unidade: {numero[0]}')
else:
    if tamanho == 2:
        print(f'Unidade: {numero[-1]}')
        print(f'Dezena: {numero[-2]}')
    if tamanho == 3:
        print(f'Unidade: {numero[-1]}')
        print(f'Dezena: {numero[-2]}')
        print(f'Centena: {numero[-3]}')
    if tamanho == 4:
        print(f'Unidade: {numero[-1]}')
        print(f'Dezena: {numero[-2]}')
        print(f'Centena: {numero[-3]}')
        print(f'Milhar: {numero[-4]}')
#print(nr_stripped)

