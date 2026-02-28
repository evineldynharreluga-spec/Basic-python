List = [1, 2, 3, 'GFG', 2.3]
print(List)

lista = ['Geeks', 'For', 'Geeks']
print('\nList containing multiple values')
print(lista)

#Creating a multidimensional list
list2 = [['Geeks', 'For'], ['Geeks']]
print('Lista Multidimensional: ', list2)
splitted = [element for row in list2 for element in row]
print('Lista Unidimensional: ', splitted)

#acessing an element from the list
# using index number
print('Acessing element from the list')
print(lista[0])
print(lista[2])

#acessing an element from the list
# using negative indexing
print('Acessing element using negative ' \
'indexing:', lista[-1])

# Trying to print the reversed list
print(List[::-1])


