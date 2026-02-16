countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from functools import reduce

conc_countries = reduce(lambda c1, c2: c1 + ", " +
                          c2, countries)
print(conc_countries + ' are north European countries.')