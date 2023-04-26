# in-place mutates our input; such as .sor()
# Returns an updated version of the original, not a copy

# In-place:
random_list = [9, 2, 10, 1, 100, 4]
random_list.sort()
# print(random_list)

# Out-of-Place:
random_list2 = [4, 7, 3, 8, 2, 5]
sorted(random_list2)
# print(random_list2)


def swap_indecies(alist, index1, index2):
    index1_value = alist[index1]
    alist[index1] = alist[index2]
    alist[index2] = index1_value


num_list = [9, 10, 1, 2]
swap_indecies(num_list, 1, 2)
# print(num_list)


def swap_indexes(alist, index1, index2):
    alist[index1], alist[index2] = alist[index2], alist[index1]
    return alist


new_list = swap_indexes([2, 5, 10, 3], 0, -1)
# print(new_list)
