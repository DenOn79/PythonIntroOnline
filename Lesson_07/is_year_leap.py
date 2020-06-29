"""
Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
"""


def is_year_leap(year):
    if year % 4 == 0 and year % 100 or year % 400 == 0:
        return True
    else:
        return False


year = int(input('Input year: '))
if is_year_leap(year):
    print(year, 'is leap')
else:
    print(year, 'is not leap')
