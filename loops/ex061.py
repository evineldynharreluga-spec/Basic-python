a1 = int(input('Introduza o primeiro termo: '))
d = int(input('Introduza a diferenca: '))
an = a1 + (10-1)*d

lista = []
lista_nova = []
resp = ''
while resp != 'Sim':
    for i in range(1, 11):
        #i = a1 + d*(i-1)
        lista.append(a1 + d*(i-1))
        #print(i)
    resp = input('Quer mostrar mais algum termo? ').capitalize()
    qtd = int(input('Quantos termos deseja mostrar? '))
    if resp == 'Sim':
        for i in range(lista[-1], qtd+1):
            lista_nova.append(lista)
    else:
        break
print(lista)


