my_list = [1, 2, 3]
my_list = ["string", 23, 1.2, 'o']
len(my_list)
my_list[1:]

my_list[:3]

my_list = my_list + [4, 5]

l = [1, 2, 3]
l.append("append me!")
l.pop()                 # NOTE: default index = -1
l.pop(0)

new_list = ['a', 'e', 'x', 'b', 'c']
new_list.reverse()
new_list.insert(1, 'z')
new_list.remove(1)
new_list.sort()

# NOTE: append vs extend
more_list = [5, 6, 7]
append_list = [1, 2, 3, 4]
append_list.append(more_list)
append_list = [1, 2, 3, 4]
append_list.extend(more_list)
append_list = [1, 2, 3, 4]
append_list = append_list + more_list

# NOTE: nested list
l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]
matrix = [l_1, l_2, l_3]
matrix[0][0]

first_col = [row for row in matrix]         # NOTE: quick snippet


i = [1, 2, 3, 4, 5]
i.index(2)

l.insert(1, "inserted")
last = l.pop()
start = l.pop(0)

l.remove("inserted")
l.reverse()
l.sort()
