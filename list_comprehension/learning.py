list_of_lists = ([1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9])

flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)


'''flattened_list = []
for row in list_of_lists:
    for number in row:
        flattened_list.append(number)
print(flattened_list)

for i in range(4):
    for j in range(3):
        print((i, j))'''




