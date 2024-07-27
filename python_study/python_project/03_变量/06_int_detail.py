#在python中。int可以表示很大的数
#通过学习  好像python中int没有限制位数了
# n1 = 9 ** 888888888
# print('n1 = ',n1,type(n1))
import sys

n1 = 0
n2 = 1
n3 = 2
n4 = 2 ** 15
n5 = 2 ** 128
#在python中system.getsizeof可以返回字节的大小，按照字节单位返回
print(sys.getsizeof(n1),'类型',type(n1))
print(sys.getsizeof(n2),'类型',type(n1))
print(sys.getsizeof(n3),'类型',type(n1))
print(sys.getsizeof(n4),'类型',type(n1))
print(sys.getsizeof(n5),'类型',type(n1))