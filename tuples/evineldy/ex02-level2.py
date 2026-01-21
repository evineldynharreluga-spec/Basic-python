
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('Milk', 'Eggs', 'Meat', 'Honey')
food_stuff_tp = fruits + vegetables + animal_products
#print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)

#slicing out the middle item
middle_items = int(len(food_stuff_lt) / 2)

print(food_stuff_lt[middle_items])

#slicing out the first three items and the last three items
first_three_items = food_stuff_tp[0:3]
last_three_items = food_stuff_tp[-3:]

print(first_three_items)
print(last_three_items)

#deleting th efood_stuff_tp completely
#del food_stuff_tp
print(food_stuff_tp)

print(food_stuff_lt)

string = 'a,e,i'
a = string.split(',')
print(a)

string = ['HTML','CSS','JavaScript']
joined = '# '.join(string)
print(joined)