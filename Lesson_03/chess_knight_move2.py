x1 = int(input('Input first coordinate of start (1 - 8): '))
i = 0
while x1 > 8:
    x1 = int(input('Out of chessboard. Try again, please: '))
    i += 1
    if i == 2:
        print('Ok, let\'s first coordinate of start is equal 1')
        x1 = 1
        break
y1 = int(input('Input second coordinate of start (1 - 8): '))
i = 0
while y1 > 8:
    y1 = int(input('Out of chessboard. Try again, please: '))
    i += 1
    if i == 2:
        print('Ok, let\'s second coordinate of start is equal 1')
        y1 = 1
        break
x2 = int(input('Input first coordinate of finish (1 - 8): '))
i = 0
while x2 > 8:
    x2 = int(input('Out of chessboard. Try again, please: '))
    i += 1
    if i == 2:
        print('Ok, let\'s first coordinate of finish is equal 3')
        x2 = 3
        break
if x2 == x1+2 or x2 == x1-2 or x2 == x1+1 or x2 == x1-1:
    y2 = int(input('Input second coordinate of finish(1 - 8): '))
    i = 0
    while y2 > 8:
        y2 = int(input('Out of chessboard. Try again, please: '))
        i += 1
        if i == 2:
            print('Ok, let\'s second coordinate of finish is equal 2')
            y2 = 2
            break
    if (x2 == x1+2 or x2 == x1-2) and (y2 == y1+1 or y2 == y1-1) or (x2 == x1+1 or x2 == x1-1) and (y2 == y1+2 or y2 == y1-2):
        print('That\'s right, knight can move like this.')
    else:
        print('Knight can\'t move like this')
else:
    print('Knight can\'t move like this')