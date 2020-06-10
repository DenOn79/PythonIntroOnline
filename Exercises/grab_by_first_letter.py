
import os  # reading from file. check is there such file as input one in the directory
file_name = input('Input file name from which you want to read: ')
current_directory = os.getcwd()
if not os.path.isfile(current_directory + '\\' + file_name + '.txt'):
    print('There is no such file:', current_directory + '\\' + file_name + '.txt')
else:
    f = open(file_name + '.txt')
    content = f.read()
    f.close()
current_directory = os.getcwd()  # get file name of file to be created and check is there such file in directory
file_name = input('Input name of file you want to create: ')
if os.path.isfile(current_directory + '\\' + file_name + '.txt'):
    replace_file = input('File exists. Do you want to replace? Y/N: ')
    if replace_file == 'N' or replace_file == 'n':
        print('Bye-bye!')
    else:
        if replace_file == 'Y' or replace_file == 'y':
            text_array = content.split()
            text_array_length = len(text_array)
            first_letter = input('The program will sort all the words which begin on the definite letter.\n'
                                 'Input the letter: ')
            f = open(file_name + '.txt', 'w')
            i = 0
            j = 1
            while i <= text_array_length - 1:
                char_list = list(text_array[i])
                if char_list[0] == first_letter or char_list[0] == first_letter.capitalize():
                    print(j, '.', ' ', text_array[i], sep='')
                    f.write(str(j) + '. ' + str(text_array[i] + '\n'))
                    j = j + 1
                i = i + 1
        f.close()
else:
    text_array = content.split()
    text_array_length = len(text_array)
    first_letter = input('The program will extract all the words beginning on the definite letter.\n'
                         'Input the letter: ')
    f = open(file_name + '.txt', 'w')
    f.write('The words from file on your letter: \n')
    i = 0
    j = 1
    while i <= text_array_length - 1:
        char_list = list(text_array[i])
        if char_list[0] == first_letter or char_list[0] == first_letter.capitalize():
            print(j, '.', ' ', text_array[i], sep='')
            f.write(str(j) + '. ' + str(text_array[i] + '\n'))
            j = j + 1
        i = i + 1
f.close()
