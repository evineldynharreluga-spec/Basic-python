import random
import time

#print(random.randrange(0,10))


computador = random.randrange(0, 5)
#print(computador)


user = int(input('Tente descobir o nr que computador' \
'escolheu'))
if computador == user:
    print('Voce ganhou!')
else:
    print(f'VOCE ERROU! EU ESCOLHI {computador}')
