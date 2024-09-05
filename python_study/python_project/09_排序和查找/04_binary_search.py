num_list = [1, 8, 10, 89, 1000, 1234]


def binary_search(my_list, find_val):
    left_index, right_index = 0, len(my_list) - 1
    find_index = -1
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        if my_list[mid_index] > find_val:
            right_index = mid_index -1
        elif my_list[mid_index] < find_val:
            left_index = mid_index + 1
        else:
            find_index = mid_index
            break
    return find_index


res_index = binary_search(num_list, 100)
if res_index == -1:
    print('没有找到该数')
else:
    print(f'找到数,对应的下标{res_index}')
