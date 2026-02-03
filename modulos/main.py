'''import mymodule

print(mymodule.generate_full_name('Evineldy', 'Nharreluga'))

from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p
print(fullname("Evineldy", 'Nharreluga'))
print(total(1, 2))
print(p['firstname'])'''

'''import sys

print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[0], sys.argv[1]))'''

from statistics import *
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
'''print(len(ages))
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))'''

import math
'''print(math.sqrt(4))
print(math.pow(2, 3))
print(math.floor(9.81))
print(math.ceil(3.14))
print(math.log10(100))'''


from math import pi
print(pi)

from math import pi, sqrt, pow, floor, ceil, log10
print(pi)
print(int(pow(2, 3)))

from math import *
print(ceil(9.8))

import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation[3])

from random import random, randint

print(random())
print(randint(5, 20))