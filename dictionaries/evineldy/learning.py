

#creating a dictionary
person = {
    'first_name': 'Evineldy',
    'last_name': 'Nharreluga',
    'age': 21,
    'country': 'Mozambique',
    'is_married': False,
    'skills': {'Networking', 'Data Science', 'Mentorship', 'Praying'},
    'address': {
        'street': 4172,
        'zipcode': 10407
    }
}

person['skills'] = list(person['skills'])

test = []
test = [{'name': 'Evineldy'}]

#print(test)

#checking dictionary size
print(len(person))

#accessing items by its key name
print(person['age'])


print(person.get('Evineldy'))

print(person.get('first_name'))
#print(person.get('source'))

#adding items to a dictionary
person['job_title'] = 'Student'
person['skills'].append('Java')
print(person)

#modifying items in a dictionary
person['first_name'] = 'Neldy'
person['age'] = 22

print(person)

#checking keys in a dictionary
print('skills' in person)

#removing items
person.pop('is_married')
print(person)


#changing a dictionary to a list of items
print(person.items())

#clearing a dictionary
#print(person.clear())
print(person)

#deleting a dictionary
#del person
print(person)

#creating a copy
person_copy = person.copy()

print(person.keys())
print(person.values())