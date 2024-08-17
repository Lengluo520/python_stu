def hi():
    n = 10
    print('n', n)


hi()


# print('n',n)


def cry():
    print('cry()')


def cry():
    print('cry()')


cry()


def f2(n1, n2):
    return n1 + n2, n1 - n2


r1, r2 = f2(3, 4)
print(f'r1={r1},r2={r2}')


# 多个形参
def sum(*args):
    print(f'args ->{args}  类型是 ->{type(args)}')
    tatal = 0
    for ele in args:
        tatal += ele
    return tatal


result = sum(1, 2)
print(result)


# 关键字可变参数
def person_info(**args):
    print(f'kwargs ->{args}   类型  ->{type(args)}')
    for arg_name in args:
        print(f'参数名 ->{arg_name}')

 
person_info(name='hsp')


def f2(name):
    print(f'f2() name的值:{name}  地址是：{id(name)}')
    name += 'hi'
    print(f'f2() name的值：{name}   地址是：{id(name)}')


print('===========')
name = 'tom'
print(f'调用f2()前 name的值：{name}  地址是：{id(name)}')
f2(name)
print(f'调用f2()前 name的值：{name}  地址是：{id(name)}')
