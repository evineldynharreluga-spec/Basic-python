#funcao sem parametros

''''def generate_full_name():
    first_name = "Evineldy"
    last_name = "Nharreluga"
    full_name = first_name + " " + last_name
    print(full_name)

generate_full_name()'''


def add_two_numbers():
    num_one = 2
    num_two = 3
    total = num_two + num_one
    #print(total)
add_two_numbers()



#retornando valores

''''def generate_full_name():
    first_name = 'Evineldy'
    last_name = 'Nharreluga'
    full_name = first_name + " " + last_name

    return full_name
print(generate_full_name())'''


''''def escrever_nome():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + " " + last_name

    return full_name
print("O seu nome completo e", escrever_nome())'''

''''def escrever_nome():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + " " + last_name
    print("O seu nome completo e ",full_name)
escrever_nome()'''


#escrevendo funcao com parametros

#1 parametro
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

#print(greetings('Evineldy'))

def add_ten(num):
    ten = 10
    return num + ten
#print(add_ten(90))

def area_of_circle(r):
    pi = 3.14
    area = pi * r ** 2
    return area
#print(area_of_circle(10))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total += i
    return total




#n = int(input('Introduza um numero: '))
#print(f'A soma dos numeros de 0 ate {n} e ', sum_of_numbers(n))


def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum

#num_one = int(input('Enter your first number: '))
#num_two = int(input('Enter the second number: '))
#print(f'A soma de {num_one} e {num_two} e ',sum_two_numbers(num_one, num_two))


''''def calcula_idade(current_year, birth_year):
    idade = current_year - birth_year
    return idade

print('========CALCULADORA DE IDADE ========')
current_year = int(input('Em que ano estas? '))
birth_year = int(input('En que ano nasceu? '))
print('Voce tem ', calcula_idade(current_year, birth_year), 'anos.')'''




''''def print_full_name(first_name, last_name):
    space = " "
    full_name = first_name + space + last_name
    return full_name

print_full_name(first_name='Evineldy', last_name='Nharreluga')
'''

''''def add_two_numbers(num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))'''

def find_even_numbers(n):
    evens = [] 
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

#print(find_even_numbers(10))


def calcula_idade(birth_year, current_year=2026):
    idade = current_year - birth_year
    return idade

#birth_year = int(input('Em que ano vc nasceu: '))
#print('Voce tem',calcula_idade(birth_year), 'anos.')


def generate_groups(team, *args):
    print(team)
    for i in args:
        print(i)
#generate_groups('Team-1', 'Evineldy', 'Pedro', 'Leao')


