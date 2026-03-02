''''# criando uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    

# criando objectos
pessoa1 = Pessoa('Ana', 20)
pessoa2 = Pessoa('Carlos', 25)

print(pessoa1.nome)
'''

''''class Person:
    def __init__(self, firstname, lastname, age, country, city):
        # self allows to attach parameter to the class
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
    

# criando um objecto de Pessoa
p = Person('Evineldy', 'Nharreluga', 22, 'Mozambique', 'Maputo')
print(p.firstname)
print(p.lastname)

print(f'{p.firstname} {p.lastname} tem {p.age} anos de idade')
'''

''''class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def person_info(self):
        return f'{self.firstname} {self.lastname} tem {self.age} anos.'

p = Person('Evineldy', 'Nharreluga', 22)
print(p.person_info())'''

# defining classes with default values to avoid errors

''''class Person:
    def __init__(self, firstname='Evineldy', 
                 lastname='Nharreluga', age=22, 
                 country='Mozambique', city='Maputo'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} tem {self.age} anos de idade. Vive em {self.city}, {self.country}.'
p1 = Person()
print(p1.person_info())

p2 = Person('Ana', 'Macarringue', 15, 'Canada', 'Ottawa')
print(p2.person_info())
'''

class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age}. Lives in {self.city}, {self.country}.'
    def add_skills(self, skill):
        self.skills.append(skill)
    def unpacking(self, skills): 
        for _ in self.skills:
            print(self.skills, end=' ')

p1 = Person('Evineldy', 'Nharreluga', 22, 'Mozambique', 'Maputo')
p1.add_skills('Java')
p1.add_skills('Python')
print(p1.person_info())
print(p1.skills)

# applying inheritance to another class
class Student(Person):
    pass

s1 = Student('Mateus', 'Cossa', 21, 'Mozambique', 'Maputo')
s2 = Student('Maria', 'Pedro', 19, 'Pemba', 'Mozambique')
print(s1.person_info())
s1.add_skills('Marketing')
s1.add_skills('IoT')
print(s1.skills)
s2.add_skills('Electronics')
s2.add_skills('Mechatronic')
print(s2.person_info())
print('Her skills are: ', s2.skills)


class Student(Person):
    def __init__(self, firstname='Evineldy', lastname='Nharreluga', age=22, country='Mozambique', city='Maputo', gender='Male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age}. {gender} lives in {self.city}, {self.country}'
    
s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skills('JavaScript')
print(s1.skills)


