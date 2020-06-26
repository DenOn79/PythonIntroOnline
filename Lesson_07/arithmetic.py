"""
Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть произведена над ними.
Функция должна вернуть результат вычислений зависящий от третьего аргумент +, сложить их; если -, то вычесть; * — умножить; / — разделить (первое на второе).
В остальных случаях вернуть строку "Неизвестная операция".
"""


def arithmetic(a1, a2, operation):
    if operation == '+':
        result = a1 + a2
    elif operation == '-':
        result = a1 - a2
    elif operation == '*':
        result = a1 * a2
    elif operation == '/':
        result = a1 / a2
    else:
        result = 'Unknown operation'
    return result


number_1 = int(input('Input first number: '))
number_2 = int(input('Input second number: '))
action = input('What operation would you like to do? (+, -, *, /): ')
print('The result:', number_1, action, number_2, '=', arithmetic(number_1, number_2, action))
