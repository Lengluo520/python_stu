mean = int(input('请输入月份:'))
if 1<mean<12:
    age = int(input('请输入年龄:'))
    if 4 <= mean <= 10:
        if 18<age<60:
            print('成人票价为：60')
        elif 0<age<18:
            print('儿童:半价')
        else:
            print('老人：三分之一的价格')
    else:
        if 18<age<60:
            print('成人：40')
        else:
            print('其他：20')
else:
    print('非有效月份')
