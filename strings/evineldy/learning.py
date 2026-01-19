
first_name = "Evineldy"
last_name = "Nharreluga"
space = " "
full_name = first_name + space + last_name
#print(full_name)

''''print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))'''

#new line escape sequence
'''
print("I hope everyone is enjoying the Python challenge. \nAre you?")

print('Days\tTopics\tExercises')
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("This is a backslash symbol (\\)")
print('In every programming language it starts with \"Hello, World!\"')
'''

#String formatting
first_name = "Evineldy"
last_name = "Nharreluga"
language = "Python"
formated_string = "I am %s %s. I teach %s" %(first_name, last_name, language)
#print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
#formated_string = "The area of circle with a radius %d is %.2f." %(radius, area)
#print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' % (python_libraries)
#print(formated_string)

#new style formatting
first_name = 'Evineldy'
last_name = 'Nharreluga'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
#print(formated_string)

a = 4 
b = 3

#print('{} + {} = {}'.format(a, b, a + b))
#print('{} / {} = {:.2f}'.format(a, b, a / b))

#String interpolation
a = 4
b = 3
#print(f'{a} + {b} = {a + b}')

#unpacking characters
language = 'Python'
a,b,c,d,e,f = language
#print(a), print(b), print(c), print(d), print(e), print(f)


first_name = 'Evineldy' 
a,b,c,d,e,f,g,h = first_name
#print(a), print(b), print(c), print(d), print(e), print(f), print(g), print(h)
#print(first_name[len(first_name) - 1])

''''last_letter = first_name[-1]
second_last = first_name[-2]
print(second_last)'''

#slicing python strings
language = 'Python'
first_three = language[0:3]
#print(first_three)
last_three = language[3:]
#print(last_three)

greeting = 'Hello, World!'
#print(greeting[::-1])

#String methods
challenge = 'thirty days of python'
#print(challenge.capitalize())
print(challenge.count('y'))
print(challenge.count('y', 7, 14))
print(challenge.endswith('on'))
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())
print(challenge.expandtabs(10))
print(challenge.rfind('g'))

web = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web)
print(result)

challenge = 'thirty days of pythonnn'
print(challenge.strip('noth'))

challenge = "thirty days of python"
print(challenge.replace('python', 'coding'))

challenge = 'thirty days of python'
print(challenge.split())
challenge = 'thirty, days, of, python'
print(challenge.split(', '))
