
file_name = input('Input file name you want to open: ')
f = open(file_name+'.txt')
content = f.read()
f.close()
print(content)
