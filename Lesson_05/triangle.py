
height = int(input('Input the height of triangle: '))
width = height*2-1
for i in range(height):
    for j in range(width):
        if i == height-1 or j == width//2 - i or j == width//2 + i:
            print('*  ', end='')
        else:
            print('   ', end='')
    print()
