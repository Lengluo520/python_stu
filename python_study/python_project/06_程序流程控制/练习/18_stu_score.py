sum = 0
sums = 0
pass_num = 0
for j in range(1, 4):
    for i in range(1, 6):
        std_score = float(input('请输入学生的成绩:'))
        sum += std_score
        avg = sum / i
    sums +=sum
print(f'成绩的总和是：{sums},平均分为：{avg}')
