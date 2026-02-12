'''def sum_numbers(nums):
    return sum(nums)

def higher_order_functions(f, lst):
    summation = f(lst)
    return summation
result = higher_order_functions(sum_numbers, [1, 2, 3])
print(result)
'''

'''def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    
result = higher_order_function('square')
print(result(3))'''


''''def saudacao():
    print('Ola!')

f = saudacao
f()
'''



''''def somatorio(a, b):
    soma = a + b
    return soma

def subtracao():
    sub = 5 - 2 - 1
    return sub



def aritmetica(x):
   
    return x ** 2
    
resultado = aritmetica('subtracao')
print(resultado(2))'''


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

def validar(function):
    def wrapper(para1, para2, para3):
        function(para1, para2, para3)
        if len(para1) > 3:
            print('ACEITE ', para1)
        raise ValueError('nome nao ACEITE porque tem caracteres ' \
        'a menos')
    return wrapper
''''
@validar
#@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')'''

''''@validar
def printar(full_name):
    print(f'I am a {full_name}')

printar('Nharreluga')'''

def decorator_teste(function):
    def wrapper(a, b):
        function(a, b)
        soma = a + b
        print(soma)
    return wrapper

@decorator_teste
def somar(x, y):
    print(f'Nr 1: {x}')
    print(f'Nr 2: {y}')

somar(2, 3)


