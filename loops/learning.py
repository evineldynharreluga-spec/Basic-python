''''count = 0
while count < 5:
    print(count)
    count = count + 1
else: 
    print(count)'''

''''count = 0
while count <= 5:
    print(count)
    count = count + 1
    #if count == 3:
     #   break'''

count = 0
while count < 5:
    if count == 3:
        count += 1
        continue
    #print(count)
    count += 1

numbers = [0, 1, 2, 3, 4, 5]
#for number in numbers:
    #print(number)

language = 'Python'
#for letter in language:
 #   print(letter)

#for i in range(len(language)):
 #   print(language[i])


''''for i in range(0, 5):
    print(i)'''

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
''''for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed 
    print(person)'''

''''numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print('loops end')
print('outside the loop')'''

''''lst = list(range(11))
print(lst)'''

''''lst = list(range(0,11,2))
print(lst)

for number in range(11):
    print(number)'''


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}



''''for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)'''

''''for number in range(11):
    print(number)

print('The loop stops at ', number)
'''

for number in range(6):
    pass