#f = open("C:/Users/Evineldy Nharreluga/Desktop/files/texto.txt")
#txt = f.read()
#print(txt)

#t = open("D:/Qt34/UEM-FENG/UEM-FENG-5TH YEAR/Coding/basic-python/file_handling/teste")
''''print(t)
texto = t.read(20)
print(texto)'''
#t.close()


#para ler apenas a primeira linha
#line = t.readline()
#print(line)
#t.close()

#ler linha por linha
''''lines = t.readlines()
print(lines)'''

#linha por linha usando splitlines
''''with open("D:/Qt34/UEM-FENG/UEM-FENG-5TH YEAR/Coding/basic-python/file_handling/teste") as t:
    spliited = t.read().splitlines()
    print(spliited)'''
    

#para nao precisar fazer o close no final evitando o esquecimento
''''with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto.txt") as f:
    texto = f.readline()
    print(type(texto))
    print(texto)
'''

#opening files for writing

''''with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto.txt", 'a') as f:
    f.write('\nThis text has to be appended at the end')

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_novo.txt", 'w') as t:
    t.write('This text will be written in a newly created file.')

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_novo.txt", 'a') as t:
    t.write('\nThis is a new text I am adding to the newly file')

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_novo.txt", 'r') as f:
    texto = f.read().splitlines()
    print(type(texto))
    print(texto)

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_novo_2.txt", 'w') as f:
    f.write('New text file .txt')

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_novo_2.txt", 'r') as f:
    texto = f.read()
    print(texto)

#it is possible to delete files
import os
if os.path.exists("C:/Users/Evineldy Nharreluga/Desktop/files/textos.txt"):
    os.remove("C:/Users/Evineldy Nharreluga/Desktop/files/textos.txt")
else:
    print('The file does not exist!')

with open("C:/Users/Evineldy Nharreluga/Desktop/files/texto_teste.txt", 'w') as d:
    texto = d.write('Testando coisas bonitas \nMas epah ha coisas feias')
    

if os.path.exists("C:/Users/Evineldy Nharreluga/Desktop/files/texto_teste.txt"):
    os.remove("C:/Users/Evineldy Nharreluga/Desktop/files/texto_teste.txt")
else:
    print('The file does not exist')'''


import json

person_json = '''{
    "name": "Evineldy",
    "country": "Mozambique",
    "city": "Maputo",
    "skills": ["Networking", "Data Science", "Mentorship"]
}
'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)

print(person_dct.keys())

habs = person_dct['skills']
print(habs)
print('Java' in habs)



