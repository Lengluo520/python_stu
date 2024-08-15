# for i in range(1,4):
#     user = input('请输入您的用户名:')
#     password = input('请输入密码:')
#     if user != '张无忌' and password != 888:
#         print(f'登录错误,还有{3-i}次机会')
#     else:
#         print('登录成功')
#         break

for i in range(1,4):
    username = input("请输入您的用户名：")
    password = input('请输入您的密码：')
    if username == '张无忌' and password == '888':
        print('登录成功')
        break
    else:
        print(f'用户名或密码输入错误，您还有{3-i}次机会')

