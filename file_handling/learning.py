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
#print(habs)
#print('Java' in habs)



numeros = [1, 2, 3, 4, 5, 6]


registos = [
    ("Evineldy", 22),
    ("Ana", 19),
    ("Carlos", 25)
]

print(registos[0])
for chave, valor in registos:
    print(f'Nome: {chave}, Idade: {valor}')

pessoa = {
    "nome": "Evineldy",
    "idade": 22,
    "curso": "Engenharia Informática"
}

for k, v in pessoa.items():
    print(k, v)

def multiplicar(a, b, c):
    return a * b * c

valores = [2, 3, 4]

resultado = multiplicar(*valores)
print(resultado)


def apresentar(nome, idade, cidade):
    print(nome, idade, cidade)

dados_json = '''{
    'nome': 'Evineldy',
    'idade': 22,
    'cidade': 'Maputo'
}'''


dados_dct = json.loads(dados_json)
print(dados_dct)
