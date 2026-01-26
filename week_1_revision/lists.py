lista  = list()
lista = []

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime', 'apple']
first_fruit, second_fruit, third_fruit, *rest = fruits

#print(second_fruit)
#print(rest)
fruits.insert(0, 'tangerina')
first_fruit = fruits[0]
#print(fruits)
#print(first_fruit)

fruits.sort(reverse=True)
#print(fruits)

empty_list = list()
players = ['Curry', 'James', 'Jordan', 'Bryant', 'Doncic', 'Jokic']
print(len(players))

length = len(players)
middle = int(length / 2)
middle_1 = int((length/2) - 1)
print(players[middle])
print(players[middle_1])

mixed_data_types = ['Evineldy', 21, 1.72, 'single', 'Maputo']
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
middle = int(len(it_companies) / 2)
print(len(it_companies))
print(middle)
print(it_companies[middle])
it_companies.append('OpenAI')
print(it_companies)
it_companies.insert(5, 'Samsung')
print(it_companies)
it_companies[0].upper()
print(it_companies[0].upper())
joined = '#; '.join(it_companies)
print(joined)
print('Facebook' in it_companies)
it_companies.sort(reverse=True)
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

to_join = front_end + back_end
print(to_join)
full_stack = to_join.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
ages.append(19)
ages.append(26)
print(ages)
tamanho = int(len(ages))
middle_1 = int(tamanho / 2)
middle_2 = int(tamanho / 2) 
print(ages[middle_1], ages[middle_1 - 1])
median = (ages[middle_1] + ages[middle_1 - 1])/2
print(median)
print(f'Sum: {sum(ages)/len(ages)}')
#median_age = ages[tamanho]
#print(median_age)
