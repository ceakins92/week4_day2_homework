def swap_indecies(list, index1, index2, index3):
    list[index1], list[index2], list[index3] = list[index3], list[index1], list[index2]
    return list


num_list = [9, 10, 1, 2, 8, 2, 11]
print(swap_indecies(num_list, 1, 2, 3))
