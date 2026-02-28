#Creating a Set with a mixed type of values

Set = set([1, 2, 'Geeks', 4, 'For', 6, 'Geeks'])
print('\nSet with the use of Mixed Values')
print(Set)

print('\nElements of set: ')
for i in Set:
    print(i, end=' ')
print()

print('Geeooks' in Set)


normal_set = set(['a', 'b', 'c'])

print('Normal set: ', normal_set)

frozen_set = frozenset(['e', 'f', 'g'])
print('Frozen Set: ', frozen_set)


