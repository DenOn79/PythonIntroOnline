
string = input('Input string: ')
h_number = string.count('h')
if h_number <= 2:
    print('There is nothing to replace. Number of h =', h_number)
else:
    first = string.find('h')
    last = string.rfind('h')
    print(string[:first + 1] + string[first + 1: last].replace('h', 'H') + string[last:])
