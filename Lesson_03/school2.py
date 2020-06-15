
i = 1
total_number_of_pupils = 0
while i <= 3:
    print('For class #', i)
    number_of_pupils = int(input('Input number of pupils in class: '))
    total_number_of_pupils += number_of_pupils
    i += 1
print(int((total_number_of_pupils+1)//2), 'desks must be bought for school.')
