
empty_tuple = ()
tupla = ('item1', 'item2')
#print(tupla)

fruits = ('banana', 'orange', 'mango', 'lemon')
''''print(fruits)
print(len(fruits))
print(fruits[0])'''
first_item = fruits[0]
second_item = fruits[1]
last_item = fruits[len(fruits) - 1]
last_fruit = fruits[-1]
#print(first_item, second_item, last_item, last_fruit)
all_items = fruits[1:2]
#print(all_items)

#if you want to change an item from an index, you can just change a tuple to a list and then do what you want
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)
fruits = tuple(fruits)
print(fruits)

#it is possible to check an item in a tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits)
print('apple' in fruits)

#joining tuples
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
print(fruits)