fruits = {'banana', 'orange', 'mango', 'lemon'}
#print(fruits)
#adding item lime
#fruits.add('lime')
#fruits.add('peach')
#print(fruits)


fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['tomato', 'potato', 'cabbage', 'onion', 'carrot']
fruits.extend(vegetables)
fruits.pop()
#print(fruits)
#print(fruits)

#adding multiple items to a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
#print(fruits)

#fruits.remove('mango')
removed = fruits.pop()
#print(removed)
#print(fruits)

#to clear a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
#print(fruits)

#to delete a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
#del fruits
#print(fruits)

#to remove an item using discard()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.discard('lime') #e arriscado porque nao lanca nenhum erro

#converting list to set to eliminate duplicated items
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) 
#print(fruits)


#joining sets using union
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
''''print(fruits.union(vegetables))
print(fruits | vegetables)'''
#finding intersection using intersection() method
whole_num = {0,1,2,3,4,5,6,7,8,9,10}
even_num = {0,2,4,6,8,10}
#print(whole_num.intersection(even_num))

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
#print(python.intersection(dragon))

#checking subset and superset
whole_num = {0,1,2,3,4,5,6,7,8,9,10}
even_num = {0,2,4,6,8,10}
''''print(whole_num.issubset(even_num))
print(even_num.issubset(whole_num))
print(even_num.issuperset(whole_num))
print(whole_num.issuperset(even_num)'''

whole_num = {0,1,2,3,4,5,6,7,8,9,10}
even_num = {0,2,4,6,8,10}


whole_num = {0,1,2,3,4,5,6,7,8,9,10}
even_num = {0,2,4,6,8,10,11}
print(whole_num.symmetric_difference(even_num))
print(even_num.symmetric_difference(whole_num))

#print(whole_num.symmetric_difference(even_num))


even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
print(even_numbers.isdisjoint(odd_numbers)) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.isdisjoint(dragon))  # False, there are common items {'o', 'n'}
