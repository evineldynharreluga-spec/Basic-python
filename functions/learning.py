def greet(name, location):
    print('Hi there', name, 'how is the weather in', location)

greet(name='Kelsy', location='Washington')


my_dict = {'name': 'Kelsy', 'location': 'washington'}

greet(**my_dict)







