from collections import Counter

#With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))

# With dictionary
count = Counter({'A': 3, 'B': 5, 'C': 2})
print(count)

count.update(['A', 1])
print(count)


from collections import OrderedDict

print('Before deleting:')
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key,':',value)

print('\nAfter deleting:')
od.pop('c')
for key, value in od.items():
    print(key, value)

print('\nAfter re-inserting:')
od['c'] = 3
for key, value in od.items():
    print(key, value)


# to join dictionaries into single one using ChainMap()

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

from collections import ChainMap
c = ChainMap(d1, d2, d3)
print()
print(c)

from collections import namedtuple

#Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

S = Student('Evineldy', 22, 13022004)

print(f'{S.name} is {S.age} years old!')


import collections

de = collections.deque([1, 2, 3])
de.append(4)

#printing modified deque
print('The deque after appending at right is:', de)

#using appendleft() to insert element at left end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print('The deque after appending at left is: ', de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print('The deque after removing at the right end:', de)

# deleting using popleft()
de.popleft()
print('After removing at the left: ', de)


from collections import UserDict
# Creating a Dictionary where deletion is not allowed

class MyDict(UserDict):

    # Function to stop deletion from dictionary
    def __del__(self, s = None):
        raise RuntimeError('Deletion not allowed')
    
    # Function to stop pop from dictionary
    def pop(self, s = None):
        raise RuntimeError('Deletion not allowed')
    
    # Function to stop popitem from dictionary
    def popitem(self, s = None):
        raise RuntimeError('Deletion not allowed')
    
#Drivers code
d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

#print('Original Dictionary', d)

d.pop(1)