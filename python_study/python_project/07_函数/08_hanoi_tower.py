def hanoi_tower(num,a,b,c):
    if num==1:
        print('第1个盘从：“a” 到 "c"')
    else:
        hanoi_tower(num-1,a,c,b)
        print(f'第{num}个盘从：{a} -> {c}')
        hanoi_tower(num-1,b,c,a)

hanoi_tower(5,"A","B","C")