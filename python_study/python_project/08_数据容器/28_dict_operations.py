dict_a = {'one': 1, 'two': 2, 'three': 3}
print(f'dict_a的元素的个数：{len(dict_a)}')
print('key为three对应的value:', dict_a['three'])
dict_a['one'] = '第一'
print(dict_a)
dict_a['four'] = 4
print(f'dict_a:{dict_a}')
del dict_a['four']
val = dict_a.pop('one')
print(f'val:{val}')
print(f'dict_a:{dict_a}')
dict_a_keys = dict_a.keys()
print(f'dict_a_keys:{dict_a_keys}')
print('two' in dict_a)
dict_a.clear()
print(f'dict_a:{dict_a}')