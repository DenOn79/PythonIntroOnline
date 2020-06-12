
number = int(input('Input integer three digit positive number: '))
ones = number//100
tens = (number//10-(((number//10)//10)*10))*10
hundreds = (number - (ones*100 + tens))*100
inverted_number = hundreds + tens + ones
print('Inverted number = ', inverted_number)