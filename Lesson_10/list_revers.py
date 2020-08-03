"""
Необходимо написать функцию которая разворачивает исходный список наоборот.

Алгоритм прост и ваши действия заключаются в следующем: мы меняем местами 0-ый элемент с последним, 1-ый с предпоследним и д.т.

Итого количество таких обменов будет равно половине длины списка. Иначе элементы поменяются местами по-второму кругу и вернутся в первоначальное положение.

Применять функцию revers() или срезы с шагом -1 нельзя. Так же, нельзя использовать дополнительные переменные (можно использовать переменную цикла for) и списки.
"""

from random import randint

lst_length = int(input('Input number of list elements: '))
lst = [randint(1, 100) for _ in range(lst_length)]


def list_reverse(lst_to_revers):
    for i in range((len(lst_to_revers) - 1)):
        lst_to_revers[i], lst_to_revers[(len(lst_to_revers) - 1) - i] = lst_to_revers[(len(lst_to_revers) - 1) - i], lst_to_revers[i]
        i += 1
        if i == (len(lst_to_revers)) // 2:
            break
    return lst_to_revers


print('Original list: ', lst)
print('Reversed list: ', list_reverse(lst))
