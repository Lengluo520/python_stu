# 双分支语句
age = int(input('请输入你的年龄：'))
if age >= 18:
    print('你的年龄已经成年，要对自己的行为负责')
else:
    print('你的年龄还未成年，就给你一次警告！')
print('========================')
x = 4
y = 1
if x > 2:
    if y > 2:
        print(x + y)
    print('你好')
else:
    print('x is ', x)

print('========================')

num1 = 5
num2 = 60
if num1 + num2 >= 50:
    print('hello world')

print('========================')
num3 = 12.2
num4 = 15.1
if num3 > 10.0 and num4 < 20.0:
    print('fnum3+num4的和为:%.2f' % (num3 + num4))

print('========================')

num3 = 12.2
num4 = 15.1
if num3 > 10.0 and num4 < 20.0:
    print(f'{num3}+{num4}的和为：{num3 + num4}')
print('========================')

num5 = int(input('请输入一个num5的值：'))
num6 = int(input('请输入一个num6的值：'))
if (num5 + num6) % 3 == 0 and (num5 + num6) % 5 == 0:
    print('可以被3和5同时整除')
else:
    print('不能被3和5同时整除')
print('========================')

year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('该年份为闰年')
else:
    print('该年份不是闰年')
