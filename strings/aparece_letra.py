''''frase = input('Escreva uma frase: ')
counter = 0

if frase.count('a') == 0:
    print('Nao contem a letra a')
else:
    print(f'A letra "a" aparece {frase.count('a')} vezes.')
    print(f'A letra "a" aparece pela primeira vez na posicao {frase.find('a')}')
    print(f'A letra "a" aparece pela ultima vez na posicao {frase.rfind('a')}')'''


nome = input('Nome completo: ')
separado = nome.split()
print(f'{separado[0]} {separado[-1]}')