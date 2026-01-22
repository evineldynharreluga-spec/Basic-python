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
print(fruits)

#to delete a set
fruits = {'banana', 'orange', 'mango', 'lemon'}
#del fruits
print(fruits)

#to remove an item using discard()
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.discard('lime') #e arriscado porque nao lanca nenhum erro

