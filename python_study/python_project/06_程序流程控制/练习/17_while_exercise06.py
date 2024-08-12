total_level = int(input('请输入金字塔的层数是一个整数:'))
for i in range(1, total_level + 1):
    for k in range(total_level - i):
        print(' ', end='')
    for j in range(i * 2 - 1):
        if j == 0 or j == 2 * (i - 1) or i == total_level:
            print('*', end='')
        else:
            print(' ', end='')
    print('')
