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
print(set(lst1))
print(set(lst2))
# print('similar values: ', set(lst1) & set(lst2))
print(len(set(lst1) - set(lst2)), ' unique values for list1: ', set(lst1) - set(lst2), '\n',
      len(set(lst2) - set(lst1)), ' unique values for list2: ', set(lst2) - set(lst1), sep='')


