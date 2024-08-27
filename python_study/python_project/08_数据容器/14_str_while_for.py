str_b = 'hi-您好，我是python'
index = 0
while index < len(str_b):
    print(f'第{index+1}个元素是->{str_b[index]}')
    index += 1

print('='*20)

for ele in str_b:
    print(ele)