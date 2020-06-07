
import os
current_directory = os.getcwd()
file_name = input('Input name of file you want to create: ')
if os.path.isfile(current_directory+'\\'+file_name+'.txt'):
    replace_file = input('File exists. Do you want to replace? Y/N')
    if replace_file == 'Y' or replace_file == 'y':
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
    else:
        if replace_file == 'N' or replace_file == 'n':
            print('Bye-bye!')
else:
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