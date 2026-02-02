num = []
resp = ''
s = 0
while resp != 'N':
        num.append(int(input('Introduza um numero: ')))
        resp = input('Quer continuar? [S/N]').upper()
        if resp not in 'NnSs':
            print('______________')
            print('Resposta invalida! ')
            print('______________')
            continue
    
print(num)
print(sum(num)/len(num), 'maior:',max(num), 'menor: ',min(num))

