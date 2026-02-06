names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
lista = []
flatten = [name for row in names for name in row]
#print(flatten)

for name in flatten:
    for i in name:
        lista.append(i)
print(lista)
