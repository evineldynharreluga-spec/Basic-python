countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

upper_countries = map(lambda country: country.upper(), countries)
print(list(upper_countries))

squared_numbers = map(lambda num: num ** 2, numbers)
print(list(squared_numbers))

upper_names = map(lambda name: name.upper(), names)
print(list(upper_names))

countries_land = filter(lambda land: 'land' in land, countries)
print(list(countries_land))

six_char_countries = filter(lambda six: len(six) == 6, countries)
print(list(six_char_countries))

six_letters_more = filter(lambda six: len(six) >= 6, 
                          countries)
print(list(six_letters_more))

countries_starts_with_E = filter(lambda country: country.startswith('E'), countries)
print(list(countries_starts_with_E))

