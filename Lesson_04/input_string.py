
string = input('Input string: ')
print('The 3-rd symbol of this string is', string[2])
print('The penultimate symbol of this string is', string[-2])
print('The five first symbols are', string[:5])
print('The string without two last symbols is', string[:-2])
print('All symbols with odd indexes are', string[::2])
print('All symbols with even indexes are', string[1::2])
print('Backward string is', string[::-1])
print('Backward string from the last symbol skipping one is', string[-1::-2])
print('Length of the string is', len(string))
