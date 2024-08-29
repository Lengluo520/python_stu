str_names = 'tom jack mary nono smith hsp'
str_names_list = str_names.split(' ')
print(f'一共有：{len(str_names_list)}人名')
print(str_names.replace('hsp','老刘'))
str_names_upper = ''
for element in str_names_list:
    if element.isalpha():
        str_names_upper += element.capitalize()+' '
print(str_names_upper.strip(' '))