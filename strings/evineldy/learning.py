
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
print("I hope everyone is enjoying the Python challenge. \nAre you?")

print('Days\tTopics\tExercises')
print("Day 1\t5\t5")
print("Day 2\t6\t20")
print("This is a backslash symbol (\\)")
print('In every programming language it starts with \"Hello, World!\"')

#String formatting
first_name = "Evineldy"
last_name = "Nharreluga"
language = "Python"
formated_string = "I am %s %s. I teach %s" %(first_name, last_name, language)
print(formated_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
#formated_string = "The area of circle with a radius %d is %.2f." %(radius, area)
#print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries: %s' % (python_libraries)
print(formated_string)