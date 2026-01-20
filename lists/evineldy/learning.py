
#How can I create lists?
#1st way
lst = list()
#print(len(lst))
#2nd way
lst = []
#print(len(lst))

fruits = ['banana','orange','mango','lemon']
vegetables = ['Tomato', 'Potato', 'Cabbge', 'Onion', 'Carrot']
animal_products = ['milk', 'meat', 'butter', 'yoghurt']
web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongoDB']
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

''''print('Fruits', fruits)
print('Number of fruits: ', len(fruits))'''

#Lists can contain different data types
lista = ['Evineldy', 21, True, {'country': 'Mozambique', 'city': 'Maputo'}]

''''print(f'{'='*3} DADOS DO ESTUDANTE {'='*3}')
print('Nome\tIdade\tPais de Origem\tCidade')
print(f'{lista[0]}\t{lista[1]}\t{lista[3]}')'''

#Acessing list items using positive index
fruits = ['Banana', 'orange', 'mango', 'lemon']
print(f'First index: {fruits[0]}')
print(f'Second index: {fruits[1]}')
print(f'Third index: {fruits[2]}')
print(f'Last index: {fruits[len(fruits)-1]}')

#Acessing list items using negative index
print(f'Last index: {fruits[-1]}')
print(f'Second last: {fruits[-2]}')
print(f'Third last: {fruits[-3]}')

#Unpacking
lista = ['item1', 'item2', 'item3']
first_item, second_item, third_item = lista
print(first_item)

first, second, third, *rest, tenth =[1,2,3,4,5,6,7,8,9,10]
print(first)
print(second)
print(tenth)
print(rest)


fruits = ['Banana', 'orange', 'mango', 'lemon']
#slicing items
all_fruits = fruits[-4:] 
orange_and_mango = fruits[-3:-1]
print(orange_and_mango)

#modifying lists
fruits[0] = 'avocado'
print(fruits)
fruits[1] = 'apple'
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)

#testing
fruits = []
resp = ''
while resp != 'N':
    fruits.append(input('Enter the name of a fruit: ')) 
    resp = input('Pretende continuar? [S/N]').upper()
print(fruits)
tamanho = len(fruits) - 1
print(f'Vc introduziu {tamanho} frutas.')
print(f'A ultima fruta introduzida foi: {fruits[tamanho]}')