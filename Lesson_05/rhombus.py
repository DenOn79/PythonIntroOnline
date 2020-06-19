
height = int(input('Input the height of rhombus. (Please, make it even): '))
while height % 2 == 0:
    height = int(input('The number is not even. Input the height of rhombus. (Please, make it even): '))
else:
    width = height
for i in range(height):
    for j in range(width):
        if i == height//2 \
                or (i == 0 and j == width//2) \
                or (i == height - 1 and j == width//2) \
                or (i <= height//2 and width//2 - i <= j <= width//2 + i) \
                or (i == height//2 + j) \
                or (i == height//2 + ((width-1) - j)):
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
