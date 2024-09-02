# 集合的常用操作
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print('basket的元素个数：', len(basket))

print('apple' in basket)

basket.add('grape')
print('basket的元素是:', basket)

basket.remove('grape')
print('basket的元素是:', basket)

ele = basket.pop()
print('ele的元素是:', ele)

books = {'天龙八部','笑傲江湖'}
books_2 = {'雪山飞狐','神雕侠侣','天龙八部'}
books_3 = books.union(books_2)
books_3 = books | books_2
print('books_3:',books_3)

books_4 = books.intersection(books_2)
print('books_4:',books_4)

books_5 = books.difference(books_2)
print('books_5:',books_5)