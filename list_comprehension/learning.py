language = 'Python'

#changing language from a string to a list
lst = []
for letter in language:
    lst.append(letter)
print(lst)

#using list comprehension
lst = [i for i in language]
print(lst)


numbers = []
for i in range(11):
    numbers.append(i)
print(numbers)

numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i  *i ) for i in range(11)]
print(numbers)

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

numbers1 = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
numbers1.sort()
positive_even_numbers = [i for i in numbers1 if i % 2 == 0 and i > 0]
print(positive_even_numbers)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)