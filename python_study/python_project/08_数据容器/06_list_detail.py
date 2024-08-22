list1 = []
list2 = list()
print(list1, type(list1))
print(list2, type(list2))

list3 = [100, 'jack', 405, 100]
print(list3)

list4 = [1, 2.1, '您好']
print(list4[2])
# print(list4[3])

list5 = [1, 2.1, '您好']
print(list5[-2])

list_a = ['天龙八部', '笑傲江湖']
print('list_a:', list_a)
list_a[0] = '雪山飞虎'
print('list_a:', list_a)
list_a.append('倚天屠龙')
print('list_a:', list_a)
del list_a[1]
print('list_a:', list_a)

list7 = [1, 2.1, '您好']
print(f'list:{list7} 地址：{id(list7)}')
list7[1] = 'python'
print(f'list:{list7} 地址：{id(list7)}')

list8 = [1, 2.1, '您好']
list9=list8
list9[2]= 500
print(f'list:{list8}')
print(f'list:{list9}')
