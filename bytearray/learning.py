#bytearray mutable sequence of integers in the range
# 0 <= x < 256

#Creating bytearray
a = bytearray((12, 8, 25, int(255.5)))
print('Creating bytearray: ')
print(a)

#acessing elements
print('\nAcessing Elements:', a[1])

#modifying elements
a[1] = 3
print('\nAfter Modifying: ')
print(a[3])

#Appending elements
a.append(30)
print('\nAfter appending Elements:')
print(a)