
number = int(input('Input the number: '))
exponent = 0
degree = 1
while degree <= number:
    degree *= 2
    exponent += 1
else:
    degree /= 2
    exponent -= 1
    print('Degree =', int(degree), '\nexponent =', exponent, '\n2 **', exponent, '=', int(degree))
