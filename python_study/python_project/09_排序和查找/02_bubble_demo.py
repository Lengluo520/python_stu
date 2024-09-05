# 冒泡排序
num_list = [24, 69, 80, 57, 13]


def bubble_sort(my_list):
    for j in range(0, 4):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(f'第一轮排序后的结果：{my_list}')

    for j in range(0, 3):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(f'第二轮排序后的结果：{my_list}')

    for j in range(0, 2):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(f'第三轮排序后的结果：{my_list}')

    for j in range(0, 1):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(f'第四轮排序后的结果：{my_list}')


my_list = [24, 69, 80, 57, 13, 90]
for i in range(0, len(my_list) - 1):
    for j in range(0, len(my_list) - 1 - i):
        if my_list[j] > my_list[j + 1]:
            my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print(f'第{i + 1}轮排序后的结果 my_list', my_list)
bubble_sort(num_list)
