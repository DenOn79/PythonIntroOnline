
i = 1
total_number_of_desks = 0
while i <= 3:
    print('For class #', i)
    number_of_pupils = int(input('Input number of pupils in class: '))
    if number_of_pupils % 2 == 0:
        number_of_desks = number_of_pupils / 2
    else:
        if number_of_pupils % 2 != 0:
            number_of_desks = (number_of_pupils + 1) / 2
    total_number_of_desks += number_of_desks
    i += 1
print(int(total_number_of_desks), 'desks must be bought for school.')
