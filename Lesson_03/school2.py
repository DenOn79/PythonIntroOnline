
i = 1
total_number_of_desks = 0
while i <= 3:
    print('For class #', i)
    number_of_pupils = int(input('Input number of pupils in class: '))
    number_of_desks = ((number_of_pupils+1)//2)
    print('For class #', i, 'must be bought', number_of_desks, 'desks.')
    total_number_of_desks += number_of_desks
    i += 1
print()
print(int(total_number_of_desks), 'desks must be bought for school.')
