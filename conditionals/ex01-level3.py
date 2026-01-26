person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    skills_list = person['skills']
    middle_item = int(len(skills_list) / 2)
    print(skills_list[middle_item])
if 'skills' in person:
    print('YES') if person.get('Python') else print('NO')
skills_set = set(skills_list)
front_end_set = {'JavaScript', 'React'}
back_end_set = {'Node', 'Python', 'MongoDB'}
full_stack_set = {'React', 'Node', 'MongoDB'}
if front_end_set.intersection(skills_set):
    print('He is a front end developer')
if back_end_set.intersection(skills_set):
    print('He is a Back end developer')
if full_stack_set.intersection(skills_set):
    print('He is a fullstack developer')
if front_end_set.intersection(skills_set) and back_end_set.intersection(skills_set) and full_stack_set.intersection(skills_set):
    print('He is a fullstack developer')
else:
    print('Unknown title!')


if person['is_married'] == True and person['country'] == 'Finland':
    print('Asabeneh Yetayeh lives in Finland. He is married.')