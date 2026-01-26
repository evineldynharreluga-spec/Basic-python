fruits = {'banana', 'mango', 'apple', 'lemon'}
print(len(fruits))
#to check an item existence
print('mango' in fruits)

vegetables = {'lettuce', 'tomato'}
fruits.union(vegetables)
fruits.update(vegetables)
print(fruits)


whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers) )


python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon


# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

it_companies.add('Twitter')

it_companies.update(['Samsung', 'SpaceX', 'Huawei', 'Tesla'])
print('Motorola' in it_companies)
#it_companies.remove('Tesla')
print('Tesla' in it_companies)

print(A.union(B).union(B.union(A)))
print(A.symmetric_difference(B))

string = 'I am a teacher and I love to inspire and teach people'
splitted = string.split()
print(splitted)
unique = set(splitted)
print(len(unique))