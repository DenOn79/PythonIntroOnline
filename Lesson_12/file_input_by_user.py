"""
 Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
Окончанием ввода пусть служит пустая строка. Каждая введённая строка, в файле, должна начинаться с новой строки.
"""
import os
current_directory = os.getcwd()
file_name = input('Input name of file you want to create: ')
first_name = input('First name: ')
last_name = input('Last name: ')
age = input('Age: ')
email = input('Email: ')
f = open(file_name+'.txt', 'w')
f.write('First name: '+first_name+'\n')
f.write('Last name: '+last_name+'\n')
f.write('Age: '+age+'\n')
f.write('Email: '+email+'\n')
f.close()
