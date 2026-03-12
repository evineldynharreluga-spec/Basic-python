from statistics import median as md
from statistics import mean as me
ages = [15, 12, 14, 13]

print(md(ages))


import numpy as np
''''print('NumPy: ', np.__version__)
print(dir(np))'''


python_list = [1, 2, 3, 4, 5]
print('Type: ', type(python_list))
print(python_list)

lista = []
two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
splitted = [lista for row in two_dimensional_list for lista in row]
print(splitted)

print(two_dimensional_list)

# Creating Numpy(Numerical Python) array from python list
numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))
print(np.array(numpy_array_from_list))

numpy_array_from_list2 = np.array(python_list, dtype=float)
print(numpy_array_from_list2)

numpy_bool_array = np.array([0, -1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)

numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array:', numpy_two_dimensional_list.tolist())


python tuple = ()