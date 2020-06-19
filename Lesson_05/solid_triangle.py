
height = int(input('Input the height of triangle: '))
width = height*2-1
for i in range(height):
    for j in range(width):
        if i == height-1 or width//2 - i <= j <= width//2 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
