import string
from random import *
def random_user_id():
    user_id = string.digits[0:3] + string.ascii_letters[5:8]
    sorted(user_id)
    
    return user_id

print(random_user_id())


'''def user_id_gen_by_user():
    
    nr_char = int(input('No. of characters: '))
    nr_ids = int(input('No. of ids: '))
    for i in range(0, nr_ids):
        print(string.ascii_letters[0:nr_char])

user_id_gen_by_user()'''



lista = []
result = string.ascii_letters + string.digits


nr_ids = int(input('No. of ids: '))
nr_char = int(input('No. of characters: '))

for j in range(0, nr_ids):
    for i in range(0, nr_char):
        pos = randint(0, len(result))
        lista.append(result[pos])
        lista_1 = ''.join(lista)
    print(lista_1)


