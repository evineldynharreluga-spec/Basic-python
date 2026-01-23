
student = {
    'first_name' :'Evineldy',
    'last_name' : 'Nharreluga',
    'gender' : 'M',
    'age' : 21,
    'marital_status': 'single',
    'skills': ['Data Science', 'Python', 'Java', 'Networking'],
    'country': 'Mozambique',
    'address': 'Hulene B'
}

print(len(student))
print(type(student['skills']))
student['skills'].append('SQL')
student['skills'].append('C#')
print(student)
print(student.keys())
print(student.values())
print(student.items())
student.pop('address')
print(student)

del student

print(student)