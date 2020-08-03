"""
Написать функцию для перевода десятичного числа в другую систему исчисления (2-36).

Небольшая подсказка. В этой задаче вам может понадобиться:
- список
- метод `revers()` (или срез [::-1], или вместо `revers()` использовать `insert()` тогда не придётся разворачивать список), чтоб развернуть список, метод `join()`
- строка `ascii_uppercase` из модуля `string` (её можно получить если сделать импорт `from string import ascii_uppercase`), она содержит все буквы латинского алфавита.
"""

from string import ascii_uppercase


def converter(num, sys):
    res = ''
    while num:
        res += BS[num % sys]
        num //= sys
    return res[::-1] or "0"


BS = '0123456789' + ascii_uppercase
num = int(input('Input the decimal number: '))
sys = int(input('Input the numeric system you would like to convert your number: '))
print(converter(num, sys))
