fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit: ')
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
else:
    print('That fruit already exists in the list')