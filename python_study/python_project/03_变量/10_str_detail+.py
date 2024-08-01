#字符串的驻留机制-在26字母的大小写,0-9,_组成的,字符长度为0或1时,字符串在编译时进行驻留,而非运行时,数字在[-5,256]的整数范围中可以驻留
#pycharm 中有一种机制 可以把所有的值变成驻留
import sys
str1 = 'hello'
str2 = 'hello'
str3 = 'hello'
print('str1的地址:',id(str1))
print('str2的地址:',id(str2))
print('str3的地址:',id(str3))

#强制驻留指向一个内存
s1 = 'abc#'
s2 = sys.intern(s1)
print(id(s1),id(s2))
