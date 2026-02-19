paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

import re
''''most_frequent_word = re.findall('i', paragraph, re.I)
print(len(most_frequent_word))
'''
separado = paragraph.split()
#print(separado)


''''for word in separado:
    print(f'{word}', len(re.findall(word, paragraph)))
'''

lista = [(word, len(re.findall(word, paragraph))) for word in separado]
print(lista)