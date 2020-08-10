"""
М х N. M и N задаёт пользователь с клавиатуры.

Обязательные условия:

матрица создаётся при помощи list comprehension. При создании, список заполняется случайными числами (используйте генератор случайных чисел)
необходимо посчитать сумму значений каждой строки (функцию sum() использовать НЕЛЬЗЯ). Сумма выводится напротив соответствующих строк
необходимо посчитать сумму значений каждой колонки (функцию sum() использовать НЕЛЬЗЯ). Сумма выводится под соответствующей колонкой
можно использовать ТОЛЬКО ОДИН, одномерный, дополнительный список
можно использовать ТОЛЬКО ОДНУ дополнительную переменную
вывод программы ДОЛЖЕН соответствовать примеру ниже (для форматирования вывода, вам понадобится функция format())
задача считается выполненной ТОЛЬКО при строгом выполнении всех условий.
"""

from random import randint

M = int(input('Please enter the number of columns: '))
N = int(input('Please enter the number of strings: '))

matrix = [[randint(10, 99) for j in range(M)] for i in range(N)]


def sum_elements_row(array, num1, num2):
    sum_lst = []
    for i in range(num1):
        sum_el = 0
        for j in range(num2):
            sum_el += array[i][j]
        sum_lst.insert(i, sum_el)
    return sum_lst


def sum_elements_col(array, num1, num2):
    sum_lst = []
    for i in range(num1):
        sum_el = 0
        for j in range(num2):
            sum_el += array[j][i]
        sum_lst.insert(i, sum_el)
    return sum_lst


for i in range(N):
    for j in range(M):
        print(' {}'.format(matrix[i][j]), end=' ')
    print('| {}'.format(sum_elements_row(matrix, N, M)[i]))

for k in range(M):
    print('{}'.format(sum_elements_col(matrix, M, N)[k]), end=' ')