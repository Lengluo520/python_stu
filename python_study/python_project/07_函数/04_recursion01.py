def test(n):
    if n > 2:
        test(n - 1)
    print('n=', n)


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n


test(4)
print(factorial(5))
