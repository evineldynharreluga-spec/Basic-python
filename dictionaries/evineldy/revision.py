#Creating a dictionary
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print('Creating a dictionary... ')
print(Dict)

#acessing an element using key
print('Acessing an element using key: ')
print(Dict[1])

#acessing an element using get()
# method
print('Acessing the first element using get method:' \
'', Dict.get('Name'))

#creation using Dictionary comprehension
myDict = {x: x**2 for x in [1, 2, 3, 4, 5]}
print(myDict)