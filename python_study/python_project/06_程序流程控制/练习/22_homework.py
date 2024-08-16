moneys = 100000
count = 0
while True:
    if moneys > 50000:
        count = count + 1
        moneys -= moneys*0.05
    elif moneys >= 1000:
        count = count + 1
        moneys -= 1000
    else:
        break
print(f'可以经过{count}个路口,剩余钱数为{moneys}')
