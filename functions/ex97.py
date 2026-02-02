def calcula_area(c, l):
    a = c * l
    print(f'A área de um terno {l}x{c} e {a}m2.')


print('Controlo de Terrenos')
print('-'*30)
#a = c * l
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
calcula_area(c, l)
 