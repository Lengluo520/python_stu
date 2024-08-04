# 赋值运算符
num1 = 100
i = 100
i += 100
print('i=', i)
i -= 100
print('i=', i)
i *= 3
print('i=', i)

print('==========================')

a = 30
b = 40
print('a=', a)
print('b=', b)
# c=a
# a=b
# b=c
# print('a=',a)
# print('b=',b)
a, b = b, a
print(a, b)

print('==========================')

c, d = 5, 2
c = c + d
d = c - d
c = c - d
print(c, d)
