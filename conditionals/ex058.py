count = 0

import random
computador = random.randrange(0, 10)
while True:
    user = int(input('Adivinhe o numero (0-10): '))
    count += 1
    if computador != user:
        print('VOCE ERROU! TENTE DE NOVO')
    else:
        break 
print('Voce acertou! Tentou ', count, ' vezes.')