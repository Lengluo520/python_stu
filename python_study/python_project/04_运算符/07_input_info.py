#input函数的使用
name = input ('请输入您的名字：')
age = int(input ('请输入您的年龄:'))
score = float(input('请输入您的成绩:'))

print('输入的信息如下：')
print(f'name:{name}\nage:{age}\nscore:{score}')  #用一行的形式写出
print('name:',name,type(name))
print('age:',age,type(age))
print('score:',score,type(score))