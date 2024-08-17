def fnb(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fnb(n - 1) + fnb(n - 2)


print(fnb(7))
