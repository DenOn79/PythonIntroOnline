"""
Дан список из чисел и индекс элемента в списке k. Удалите из списка элемент с индексом k, сдвинув влево все элементы, стоящие правее элемента с индексом k.
Программа получает на вход список (можно сгенерировать при помощи генератора случайных чисел), затем число k.
Программа сдвигает все элементы, а после этого удаляет последний элемент списка при помощи метода pop() без параметров.
Программа должна осуществлять сдвиг непосредственно в списке, а не делать это при выводе элементов. Также нельзя использовать дополнительный список.
Также не следует использовать метод pop(k) с параметром или оператор del.
"""
import random

length = 10
lst = [random.randint(10, 50) for _ in range(length)]
print(lst)
k = int(input('Input index(0 - 9): '))
for indx in range(k+1, length):
    lst[indx], lst[indx-1] = lst[indx-1], lst[indx]
    indx += 1
lst.pop()
print(lst)