"""
Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года,
которому этот месяц принадлежит (зима, весна, лето или осень).
"""


def season(month):
    if 3 <= month <= 5:
        season = 'Spring'
    elif 6 <= month <= 8:
        season = 'Summer'
    elif 9 <= month <= 11:
        season = 'Autumn'
    else:
        season = 'Winter'
    return season


month_number = int(input('Input the number of month (1 - 12): '))
while month_number > 12:
    month_number = int(input('Try again. Input the number of month (1 - 12): '))
print(month_number, 'month is the month of', season(month_number))
