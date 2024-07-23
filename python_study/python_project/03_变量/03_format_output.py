age = 80
score = 77.5
gender = '男'
name = '贾某'

#%格式化输出
print('人员信息：%s %d %.2f-%s'%(name,age,score,gender))

#format()函数
print('人员信息：{}-{} {}'.format(name,age,gender))

#f-strings
print(f'人员信息：{name}-{age} {score} {gender}')
