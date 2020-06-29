"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень).
"""


def season(month):
    if month in (3, 4, 5):
        season = 'Spring'
    elif month in (6, 7, 8):
        season = 'Summer'
    elif month in (9, 10, 11):
        season = 'Autumn'
    elif month in (12, 1, 2):
        season = 'Winter'
    return season


month_number = int(input('Input the number of month (1 - 12): '))
while month_number > 12:
    month_number = int(input('Try again. Input the number of month (1 - 12): '))
print(month_number, 'month is the month of', season(month_number))
