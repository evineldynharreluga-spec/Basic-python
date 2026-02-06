countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten = [country for row in countries for country in row]
lista = []
listaa = []
#print(flatten)
for i in flatten:
    listaa.append(list(i))
#print(listaa)

for flat in flatten:
    for flat_in in flat:
        lista.append(flat_in)
maiusculas = [elemento.upper() for elemento in lista]
other = []
print(lista)

''''for i in maiusculas:
    other.append(i[:3])
print(other)'''


