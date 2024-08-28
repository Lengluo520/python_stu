# 字典的使用
tel = {'jack':4098,'tom':4139}
print(tel,type(tel))
print('jack的tel:',tel['jack'])

dict_a = {
            'jack':[100,200,300],
            'mary':[10,20,'hello'],
            'nono':{'apple','pear'},
            'smith':'计算机老师',
            '周星驰':{
                '性别':'男',
                'age':18,
                '地址':'香港'
            }
}
print(f'dict_a:{dict_a}  类型:{type(dict_a)}')

# 字典的遍历
print('='*30)
dict_b = {'one':1,'two':2,'three':3}
for key in dict_b:
    print(key,dict_b[key])

print('=' * 30)

for value in dict_b.values():
    print(f'value:{value}')

print('=' * 30)
for key,value in dict_b.items():
    print(f'key:{key},value:{value}')

dict_c = {}
dict_d = dict()
print(f'dict')