person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(person.get('first_name'))
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)


dog = dict()
dog['name'] = 'Doug'
dog['color'] = 'Black'
dog['breed'] = 'Boerbull'
dog['age'] = 2

print(dog)
