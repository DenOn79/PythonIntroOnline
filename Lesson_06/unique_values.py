"""
Даны два списка чисел (можно сгенерировать при помощи генератора случайных чисел).
Посчитайте, сколько уникальных чисел содержится одновременно как в первом списке, так и во втором.
Примечание. Эту задачу можно решить в одну строчку.
"""
import random

length = 10
lst1 = [random.randint(10, 20) for _ in range(length)]
lst2 = [random.randint(10, 20) for _ in range(length)]
print(lst1)
print(lst2)
# One string solution:
list_unique = [i for i in (lst1+lst2) if (lst1+lst2).count(i) == 1]
# Output:
print(list_unique, '\nIn both lists there are', len(list_unique), 'unique values.')
