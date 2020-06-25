"""
Дан список целых чисел (можно сгенерировать при помощи генератора случайных чисел), число k и значение C.
Необходимо вставить в список на позицию с индексом k значение C, сдвинув все элементы, с индексом большим k, вправо.
Поскольку при этом количество элементов в списке увеличивается, в конец списка нужно будет добавить новый элемент (любое значение),
используя метод append().
Вставку необходимо осуществлять уже в считанном списке, не делая этого при выводе и не создавая дополнительного списка.
Использовать метод insert() не разрешается.

"""
import random

length = 10
lst = [random.randint(10, 50) for _ in range(length)]
print(lst)
k = int(input('Input index (0 - 9): '))
C = int(input('Input the value C: '))
lst.append(C)
for i in range((len(lst) - 1), k, -1):
    lst[i-1], lst[i] = lst[i], lst[i-1]
    i -= 1
print(lst)
