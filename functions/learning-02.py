#sem parametros
''''def lin():
      #print('-'*30)

lin()
#print('APRENDENDO PYTHON')
lin()'''

#Funcoes com 1 parametro
''''def titulo(txt):
    print('-' * 30)
    print(txt)
    print('-' * 30)'''


#titulo('APRENDENDO PYTHON!')

''''def soma(a, b):
    s = a + b
    print(s)
     

soma(a=4, b=5)
soma(4, 11)'''

 
#e possivel passar tamanho desconhecido como *num

''''def contador(*num):
    for nrs in num:
        print(nrs, end=' ')

contador(2, 3, 4, 5) '''

#functions with lists

dobrados = []
valores  = []
def dobra(valores):
    for num in valores:
       dobrados.append(num*2)
    print(dobrados)


def lin():
    print('-' * 30)


lin()
print('DOBRADOR DE NUMEROS')
lin()

resp = ''
while resp in 'Ss':
    valores.append(input('Introduza uma lista de numeros: '))
    resp = input('Quer continuar? [S/N]').upper()
    break
print('A TUA LISTA NORMAL E: ',valores)
dobra(valores)
print(dobrados)
lin()

#valores = [0, 2, 4]
#dobra(valores) 
