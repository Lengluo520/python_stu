'''
用F8 逐行执行代码
用F7 进入方法/函数内
用shift F8 跳出方法/函数
用F9 直接执行到下一个断点
'''
sum = 0
for i in range(0,10):
    sum = sum + i
    print(f'i={i}')
    print(f'sum={sum}')

print('end.....')