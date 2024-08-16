# 函数的使用
def cry():
    print('小猫，喵喵叫...')


cry()


def cal01():
    sum = 0
    for i in range(1, 1001):
        sum += i
    print('sum=', sum)


cal01()


def cal02(n):
    sums = 0
    for i in range(1, n + 1):
        sums += i
    print(sums)


cal02(5)


def get_sum(num1, num2):
    sum = num1 + num2
    print(sum)


get_sum(5, 10)
