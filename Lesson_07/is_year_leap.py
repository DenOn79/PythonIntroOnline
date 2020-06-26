"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""


def is_year_leap(year):
    if year % 4:
        return False
    else:
        return True


year = int(input('Input year: '))
print(is_year_leap(year))
