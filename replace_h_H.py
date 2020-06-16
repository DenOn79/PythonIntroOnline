
string = input('Input the sentence which contains at least three letters \'h\' (e.g. \'She holds her head so high!\'): ')
first = string.find('h')
last = string.rfind('h')
print(string[:first+1] + string[first+1: last].replace('h', 'H') + string[last:])
