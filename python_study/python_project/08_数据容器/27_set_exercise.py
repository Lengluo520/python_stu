s_history = {'小明','张三','李四','王五','Lily','Bob'}
s_politic = {'小明','小花','小红','二狗子'}
s_english = {'小明','Lily','Bob','Davil','李四'}

print(f'学生总数：{len(s_history|s_politic|s_english)}人')
print(f'只选了第一个学科的学生数量：{len(s_history-s_politic-s_english)} 和学生名字：{s_history-s_politic-s_english}')
s1 = s_history-s_politic-s_english
s2 = s_english-s_politic-s_history
s3 = s_politic-s_history-s_english
print(f'只选了一门学科的学生数量：{len(s1|s2|s3)}个，和学生的名字：{s1|s2|s3}')

print(f'选三科的学生数量:{len(s_history & s_english & s_politic)}个,学生为：{s_history & s_english & s_politic}')