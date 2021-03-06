"""
Используя выражение генератор-списка (list comprehension) сформировать словарь символов с кодами от 32 до 127 включительно.
Ключём словаря должно быть число (код символа), а значение - символ, соответствующий этому коду.
Вам понадобится функция chr(x) которая принимает в качестве параметра целое число (код символа), а возвращает символ соответствующий этому числу.

Задача решается в одну строку.
"""

char_dict = {i: chr(i) for i in range(32, 128)}

print(char_dict)
