height = float(input('请输入你的身高：'))
money = float(input('请输入你的财富:'))
sui = input('是否为帅:')
if height >= 180 and money >= 10000000 and sui == '是':
    print('我一定嫁给你')
elif height >= 180 or money >= 10000000 or sui == '是':
    print('嫁吧，比上不足，比下不余')
else:
    print('不嫁')