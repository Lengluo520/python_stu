n1 = float(input('请输入一个数：'))
n2 = float(input('请输入一个数：'))
oper = input('请输入运算符(‘+，‘-’，‘*’，’/‘):')
res = 0
if oper == '+':
    res = n1 + n2
elif oper == '-':
    res = n1 - n2
elif oper == '*':
    res = n1 * n2
elif oper == '/':
    res = n1 / n2
else:
    print('输入的符号不正确!')
print(n1,oper,n2,'=',res)