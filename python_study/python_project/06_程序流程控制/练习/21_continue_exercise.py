#continue的使用
for i in range(0,2):
    for j in range(1,4):
        if j ==2:
            continue
        print(f'i=',{i},'j=',{j})