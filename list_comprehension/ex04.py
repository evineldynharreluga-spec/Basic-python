''''countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]



from pprint import pprint
output = [[item[0][0].upper(), item[0][0][:3].upper(), item[0][1].upper()] for item in countries]
pprint(output)'''


def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)