list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [number for row in list_of_lists for number in row]
print(flatten_list)