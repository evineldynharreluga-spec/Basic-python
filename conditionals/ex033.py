maior = 0
menor = 0
temp = 0

n1 = int(input('Enter the first number: '))
n2 = int(input('Enter the second number: '))
n3 = int(input('Enter the third number: '))

if (n1 > n2) and (n1>n3):
    maior = n1
    if (n2 > n3):
        menor = n3
    else:
        menor = n2
    print('O maior e ', maior, ' e menor e ',menor)
elif (n2 > n1) and (n2>n3):
    maior = n2
    if (n1 > n3):
        menor = n3
    else:
        menor = n1
    print('O maior e ', maior, ' e o menor e ',menor)
elif (n3>n1) and (n3>n2):
    maior = n3
    if (n1 > n2):
        menor = n2
    else:
        menor = n1
    print('O maior e ', maior, ' e o menor e ', menor)
