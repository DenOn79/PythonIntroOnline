"""
Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
периметр квадрата, площадь квадрата и диагональ квадрата.
"""
import math


def square(square_side):
    result = (square_side * 4, square_side ** 2, math.sqrt(2 * (square_side ** 2)))
    return result


square_side = int(input('Input square side: '))
print('Perimeter =', square(square_side)[0], '\nArea =', square(square_side)[1], '\nDiagonal =', round(square(square_side)[2], 2))
