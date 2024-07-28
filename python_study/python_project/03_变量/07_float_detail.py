#浮点类型的表示形式
#浮点类型计算后，会存在精度损失
import sys
from decimal import Decimal
n1 = 4.5
n2 =-3.6
n3 = .512
n4 = 5.12e2
n5 = 5.12e-2
print('n1 = ',n1)
print('n2 = ',n2)
print('n3 = ',n3)
print('n4 = ',n4)
print('n5 = ',n5)
print(sys.float_info)
print(sys.int_info)

b = 8.1 / 3
print('b = ',b)

c = Decimal('8.1') / 3
print(c)