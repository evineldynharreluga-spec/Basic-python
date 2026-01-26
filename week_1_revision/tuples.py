
tupla = tuple()
tupla = ()
#print(tupla)


#convert and remember to convert it back
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
#print(fruits)
fruits = tuple(fruits)
#print(fruits)

empty_tuple = tuple()
bros = ('Deverton', 'Neldy')
sis = ('Delicia', 'Kelsy')
siblings = bros + sis
print(len(siblings))

#siblings_copy = siblings.copy()

family_members = list(siblings)
print(family_members)
family_members.insert(0, 'Antonio')
family_members.insert(1, 'Odete')
print(family_members)
family_members = tuple(family_members)
print(family_members)
print(siblings)

parents = ('Antonio', 'Odete')

