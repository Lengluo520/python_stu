list_a = [100,200,300,400,500]
print('列表中元素的个数：',len(list_a))
print('列表中最大元素:',max(list_a))
print('列表中最小元素:',min(list_a))

list_a.append(900)  #在末尾添加一个元素
print('list_a:',list_a)

list_b = [1,2,3]   #在末尾添加多个元素
list_a.extend(list_b)
print(list_a)


print(list_a.index(400))   #从列表中找出第一个匹配的值  用的是索引序列 从0开始

list_a.reverse()
print(list_a)    #反转列表

list_a.insert(4,666)   #在指定位置添加元素
print(list_a)
