hens = [3,5,1,3.4,2,50]
total_weight = 0.0
for i in hens:
    total_weight += i
    avg = total_weight/6
print('总体重为：',total_weight)
print('平均体重为：',round(avg,2))