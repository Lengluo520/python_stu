#隐式转换
var1 = 1
print(type(var1))
var1 = 1.1
print(type(var1))
var1 = '你好'
print(type(var1))

#在运算中,数据类型会向高进度转换
var2 = 10
var3 = 1.2
var4 = var2 + var3
print('var4 = ' , var4 , 'var4的类型为:',type(var4))
var2 = var2 + 0.1
print('var2 = ' , var2 , 'var2的类型为:',type(var2))

#强制转换/显示转换
i = 10
j = float(i)
print(j,type(j))
k = str(i)
print(k, type(k))
n1 = 100
n2 = 123.56
print(str(n1),type(str(n1)))
print(str(n2),type(str(n2)))
print(float(n1))
print(int(n2))
#字符串转换数值
n3 = '12.3'
print(float(n3))
# # print(int(n3))  如果字符串中原来是浮点形式的 就不能转整型
# n4 = 'hello'
# print(float(n4))
# print(int(n4))
