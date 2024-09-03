clerks = {
    '0001': {
        'age': 20,
        'name': '贾宝玉',
        'entry_time': '2011-11-11',
        'sal': 12000
    },
    '0002': {
        'age': 21,
        'name': '薛堡主',
        'entry_time': '2015-12-12',
        'sal': 10000
    },
    '0010': {
        'age': 18,
        'name': '林黛玉',
        'entry_time': '2018-10-10',
        'sal': 20000
    }
}

print(f'员工号为0010的信息为:'
      f'名字:{clerks["0010"]["name"]}\t'
      f'年龄:{clerks["0010"]["age"]} '
      f'入职时间:{clerks["0010"]["entry_time"]} '
      f'薪水:{clerks["0010"]["sal"]}')

clerks['0020'] = {
    'age': 30,
    'name': '你好',
    'entry_time': '2020-08-10',
    'sal': 6000
}
print('clerks:', clerks)

del clerks['0001']
print('=' * 320)
print('clerks:', clerks)

clerks['0020']['name'] = '李四'
clerks['0020']['entry_time'] = '1999-10-10'
clerks['0020']['sal'] += clerks['0020']['sal'] * 0.1
print('clerks:',clerks)
print('=' * 320)

keys = clerks.keys()
for key in keys:
    clerks[key]['sal'] += clerks[key]['sal'] * 0.2
print('clerks:', clerks)
print('=' * 320)

for key in keys:
    print(f'员工号为：{key}的信息如下： '
          f'年龄：{clerks[key]["age"]}'
          f'入职时间:{clerks[key]["entry_time"]}'
          f'薪水:{clerks[key]["sal"]}')
