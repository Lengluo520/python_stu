# 逻辑运算符的使用
a = 10
b = 20
print(a and b)
print(a or b)
print(not (a and b))
print('==========================')
score = 70
if (score >= 60 and score <= 80):
    print('成绩不错~')
print('==========================')
a = 1
b = 99
print(a and b)
print((a > b) and b)
print((a < b) and b)
print('==========================')
if (score <= 60 or score >= 80):
    print('成绩不错~')
print('==========================')
print(a or b)
print((a > b) or b)
print((a < b) or b)
print('==========================')
c = 3
d = not (a > 3)
print(d)
print(not False)
print(not True)
print(not 0)
print(not None)
print(not 'jack')
print(not 1.88)
print(not c)
