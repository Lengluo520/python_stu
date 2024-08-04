# 三元运算符
a = 10
b = 80
max = a if a > b else b
print('max=', max)

print('==========================')

a, b, c = 10, 20, 30
max = a if a > b else b
max = b if b > c else c
print('max=', max)

print('==========================')
max = (a if a > b else b) if b > c else c
print('max=', max)