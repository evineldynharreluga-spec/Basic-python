''''estudantes = []

while True:
    print("=================================")
    print(" SISTEMA DE GESTÃO DE ESTUDANTES ")
    print("=================================")
    print("1. Registrar estudante")
    print("2. Listar estudantes")
    print("3. Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        id_estudante = input("Codigo de Estudante: ")
        nome = input("Nome: ")        
        curso = input("Curso: ")
        nota = int(input("Nota: "))
        estudante = {
            "id_estudante": id_estudante,
            "nome": nome,
            "curso": curso,
            "nota": nota
        }

        estudantes.append(estudante)
        print("Estudante registrado!")

            
    elif opcao == "2":
        for e in estudantes:
            print(e)

    else:
        opcao == "3"
        break'''

'''nota = 15

if nota >= 10 and nota < 14:
  print("Passou!")
elif nota >= 14:
  print("Excelente!")
elif nota < 10:
  print("Reprovou!")
      '''

import math
temperaturas = [32, 29, 35, 31, 28, 33, 30]

total = 0
for t in temperaturas:
    total += t
print(total)
t_media = total/len(temperaturas)
print(f'Temperatura media: {t_media:2f}')

for t in temperaturas:
    if t > t_media:
        print(t)
        




