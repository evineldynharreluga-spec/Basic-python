#Map function

#map(function, iterable)
''''numbers = []
lista = []
for y in range(6):
    lista = numbers.append(int(input(('Nr: '))))
print(lista)

#x = [1, 2, 3, 4, 5]
def square(x = list):
    return x ** 2
numbers_squared = map(square, lista)
print(list(numbers_squared))

numbers_squared = map(lambda x: x ** 2, numbers)
print(list(numbers_squared))'''


numbers_str = ['1', '2', '3', '4', '5']
numbers_int = map(int, numbers_str)
#print(list(numbers_int))

''''names = ['Evineldy', 'Nharreluga']

def change_to_upper(x):
    return x.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))

name_upper_cased = map(lambda x: x.upper(), names)
print(list(name_upper_cased))'''


''''names = ['Evineldy', 'Nharreluga']

names_uppered = map(lambda name: name.upper(), names)
print(list(names_uppered))

def upper_names(name):
    return name.upper()

names_uppered = map(upper_names, names)
print(list(names_uppered))

'''

#Filter function

numbers = [1, 2, 3, 4, 5]

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

def is_odd(numbers):
    if numbers % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))


names = ['Evineldy','Asabeneh', 'Lidya', 'Ermias', 'Abraham']

def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))


# Map - usada para transformar valores de uma lista em outros
# transformacao
nums = [1, 2, 3, 4, 5]
print(list(map(lambda num: num ** 2, nums)))

nomes = ['Evineldy', 'Nharreluga']
print(list(map(lambda nome: nome.upper(), nomes)))


#Filter - selecciona elementos que satisfazem uma condicao
print(list(filter(lambda num: num % 2 == 0, nums)))

#reduce - somatorio de todos os valores
from functools import reduce
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)