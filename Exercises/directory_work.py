
import os
path = os.getcwd()
print ("current directory is: %s" % path)
file_name = input('Input filename you want to find in this directory: ')
if os.path.isfile(path+'\\'+file_name+'.txt'):
    print('File exists!')
else:
    print("No such file!")
