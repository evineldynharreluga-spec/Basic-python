import random


nome_aluno = list()
for i in range(0,4):
    nome_aluno.append(input(f'Introduza o nome do {i+1}o. aluno: '))
    
escolha = random.randint(1,5)
print(nome_aluno)


nome_aluno.sort(reverse=True)


print(nome_aluno)
print(f'Os nomes dos alunos sao: {nome_aluno}')
print(f'Ordem de apresentacao: {nome_aluno}')
print(f'E o aluno escolhido para apagar o quadro foi {nome_aluno[escolha]}')
