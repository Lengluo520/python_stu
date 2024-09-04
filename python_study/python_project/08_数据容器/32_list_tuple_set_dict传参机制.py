def f1(my_list):
    print(f'f1() my_list: {my_list} 地址是：{id(my_list)}')
    my_list[0] = 'jack'
    print(f'f1() my_list: {my_list} 地址是：{id(my_list)}')


my_list = ['tom','mary','hsp']
print(f'my_list: {my_list} 地址是: {id(my_list)}')
f1(my_list)
print(f'my_list: {my_list} 地址是: {id(my_list)}')