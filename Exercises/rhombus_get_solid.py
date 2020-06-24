import os
from time import sleep

height = int(input('Input the height of rhombus. (Please, make it even): '))
while height % 2 == 0:
    height = int(input('The number is not even. Input the height of rhombus. (Please, make it even): '))
else:
    width = height
for level in range(1, height - 1):
    os.system('CLS')  # clear
    for i in range(height):
        for j in range(width):
            if (
                    (i == 0 and j == width//2)
                    or (i == height - 1 and j == width//2)
                    or (i <= height//2 and j == width//2 - i or j == width//2 + i)
                    or (i == height//2 + j)
                    or (i == height//2 + ((width-1) - j))
                    or (level == i and level <= height//2 and width//2 - i <= j <= width//2 + i)
                    #  or (level == i and level > height // 2 and j == ((i - width//2)+1))
                    or (level == i and level > height // 2 and j == (i - width // 2)
            ):
                print('*  ', end='')
            else:
                print('   ', end='')
        print()
    sleep(1)
