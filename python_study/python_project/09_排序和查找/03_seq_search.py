names_list = ['白眉鹰王', '金毛狮王', '紫霞龙王', '青翼蝙王']
find_name = '金毛狮王'
res_index = names_list.index(find_name)
print('res_index', res_index)


def seq_search(my_list, find_val):
    find_index = -1
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            print(f'恭喜,找到对应的值{find_val} 下标是{i}')
            find_index = i
            break
    else:
        print(f'没有找到{find_val}')
    return find_index


res_index = seq_search(names_list, find_name)
print('res_index', res_index)


def seq_search2(my_list, find_val):
    find_index = []
    for i in range(len(my_list)):
        if my_list[i] == find_val:
            find_index.append(i)
    return find_index


res_index = seq_search2(names_list, find_name)
print('res_index', res_index)
