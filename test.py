my_list = [[1, 3], [4, 2], [2, 5], [6, 1], [8, 3]]
list = [1, 2, 3, 4, 5, 6, 7, 8.9]
sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)


for i in my_list[10:]:
    print(i)
