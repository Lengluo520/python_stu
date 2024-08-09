i = 1
count = 0
sum = 0
while i <=100:
    if i%9==0:
        print(f'{i}是9的倍数:')
        count=count+1
        print(f'累计的个数为:{count}个')
        sum +=i
        print(f'他们的总和为{sum}')
    i+=1

