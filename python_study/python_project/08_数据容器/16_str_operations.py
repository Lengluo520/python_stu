print('='*30)
str_names = 'jack tom mary hsp'
print(f'{str_names} 有{len(str_names)}个字符')
print('='*30)

str_names_new = str_names.replace('jack', '杰克',1)
print('str_names_new:',str_names_new)
print(str_names)