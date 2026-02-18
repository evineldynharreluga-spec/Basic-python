''''try:
    print(10 + '5')
except:
    print('Something went wrong')'''
from datetime import datetime
now = datetime.now()
year = now.year

''''try:
    name = input('Enter your name: ')
    year_born = int(input('Year you were born: '))
    age = year - year_born
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('Zero division error occured')
else:
    print(f'You are {name}. And your age is {age}.')'''

''''try:
    name = input('Enter your name: ')
    year_born = input('Year you born: ')
    age = year - year_born
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)
'''

''''def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))
'''

''''countries = ['Finland', 'Sweden', 'Norway', 
             'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)   '''   #  1 [2, 3, 4, 5, 6] 7

''''def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} years old.'

dct = {'name': 'Evineldy', 
       'country': 'Mozambique',
        'city':'Maputo',
        'age': 22}

print(unpacking_person_info(**dct))
'''

def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 3, 4 ,5 ,102))


for index, item in enumerate([20, 30, 40]):
    print(index, item)

countries = ['Finland', 'Sweden', 'Norway', 
             'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}.')

names = ['Finland', 'Sweden', 'Norway', 'Denmark',
         'Iceland', 'Estonia', 'Russia']
first_five = []
def unpacking_first_five_countries(names):
    for index, item in enumerate(names):
        first_five.append(item)
        if index == 6:
            ru = item
        if index == 5:
            es = item
    return first_five

print(unpacking_first_five_countries(names))
