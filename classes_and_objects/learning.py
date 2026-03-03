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




class Carro:
    
    def __init__(self, marca, modelo, preco):
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.pecas = []
    def criarCarro(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nPreco: {self.preco}'
    def adicionarPecas(self, peca):
        self.pecas.append(peca)
        

c1 = Carro('Mercedes', 'Benz', 2000000)
print(c1.criarCarro())


c1.adicionarPecas('janta')
c1.adicionarPecas('pneu')
c1.adicionarPecas('vidros fumados')
print(c1.pecas)

class Viatura(Carro):

    def __init__(self, marca, modelo, preco, importado):
        self.importado = importado
        super().__init__(marca, modelo, preco)
    def criarCarro(self):
        importado = 'Sim' if self.importado=='S' else 'Nao'
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nPreco: {self.preco}\nImportado: {importado}'

v1 = Viatura('BMW', 'x6', 30000000, 'S')
v1.adicionarPecas('pneu')
v1.adicionarPecas('jantes')
print(v1.criarCarro())
print(v1.pecas)


print('===SISTEMA DE GESTAO DE VIATURAS====')
print('===MENU===')
print('[1] Adicionar viatura')
print('[2] Remover viaturas')
print('[3] Ver viaturas adicionadas')
opcao = input('Escolha uma opcao: ')

if opcao == '1':
    #Adicionar viatura
    print('\n=======REGISTRO DE VIATURAS========')
    marca = input('Introduza a marca do carro: ')
    modelo = input('Introduza o modelo: ')

    #Adicionar preco
    while True:
        try:
            preco = float(input('Introduza o preco: '))
            break   
        except ValueError:
            print('Preco invalido. Introduza novamente.')
            

    #Importado ou nao
    while True:
        importado = input('O carro e importado? [S/N]').upper()
        if importado in ('S', 'N'):
            break
        print('Resposta invalida!')
    v2 = Viatura(marca, modelo, preco, importado)

    # Adicionar pecas
    print('\n====ADICIONAR PECAS====')
    while True:
        peca = input('Adicionar peca (ou ENTER para nao introduzir): ')
        if peca == '':
            break
        v2.adicionarPecas(peca)
print('VIATURA INTRODUZIDA!')

    
''''if opcao == '3':
    # Dados da Viatura'''
print('\n===DADOS DA VIATURA===')
print(v2.criarCarro())
print('Pecas: ', v2.pecas)
 
        
   
