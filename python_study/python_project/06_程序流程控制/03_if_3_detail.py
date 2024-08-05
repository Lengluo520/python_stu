# 多分支语句结构使用
score = float(input('请输入成绩:'))
if score >=0 and score <= 100:
    if score == 100:
        print('奖励BMW一辆')
    elif score > 80 and score < 99:
        print('奖励一台iphone13')
    elif score > 60 and score < 80:
        print('奖励一个iPad')
    else:
        print('给一个大逼兜')
else:
    print('不是正确的成绩')
