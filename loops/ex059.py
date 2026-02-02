def menu():
    print('===MENU===')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] sair do programa')
    opcao = int(input('Escolha uma opcao: '))
    while opcao != 5: 
        n1 = int(input('Introduza um numero: '))
        n2 = int(input('Introduza um numero: '))
        if opcao == 1:
            print('A soma entre n1 e n2 e ',n1 + n2)
            break
        elif opcao == 2:
            print('O produto entre n1 e n2 e ', n1 * n2)
            break
        elif opcao == 3:
            if n1 > n2: print('O maior e ', n1, ' e o menor e ', n2)
            else: print('O maior e ', n2, ' e o menor e ', n1)
            break


while True:
    print('===MENU===')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] sair do programa')
    opcao = int(input('Escolha uma opcao: '))
    while opcao != 5: 
        n1 = int(input('Introduza um numero: '))
        n2 = int(input('Introduza um numero: '))
        

        if opcao == 1:
            print('A soma entre n1 e n2 e ',n1 + n2)
            break
        elif opcao == 2:
            print('O produto entre n1 e n2 e ', n1 * n2)
            break
        elif opcao == 3:
            if n1 > n2: print('O maior e ', n1, ' e o menor e ', n2)
            else: print('O maior e ', n2, ' e o menor e ', n1)
            break
        elif opcao == 4:
            ''''n1 = int(input('Introduza um numero: '))
            n2 = int(input('Introduza um numero: '))'''
            menu()
            break
    else:
        break