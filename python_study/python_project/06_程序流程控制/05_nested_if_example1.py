score = float(input('请输入成绩:'))
if score > 8.0 :
    print('进入决赛')
    gender = input('请输入性别:')
    if gender == '男' :
        print('进入男子组')
    else:
        print('进入女子组')
else:
    print('淘汰')