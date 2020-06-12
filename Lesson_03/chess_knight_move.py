
x1 = int(input('Input first coordinate of start (1 - 8): '))
i = 0
while x1 > 8:
    x1 = int(input('Out of chessboard. Try again, please: '))
    i += 1
    if i == 3:
        print('Are you stupid? Chessboard is only 8x8. Ok, let\'s first coordinate is equal 1')
        x1 = 1
        break
y1 = int(input('Input second coordinate of start (1 - 8): '))
i = 0
while y1 > 8:
    y1 = int(input('Out of chessboard. Try again, please: '))
    i += 1
    if i == 3:
        print('You kidding?? Didn\'t get it?? ONLY 8x8. Ok, let\'s second coordinate is equal 1 too')
        y1 = 1
        break
x2 = int(input('Just try to do it again. It\'s really easy. Any number from 1 to 8, the first coordinate of finish: '))
i = 0
while x2 > 8:
    x2 = int(input('Out of this goddamn chessboard!! Try again!: '))
    i += 1
    if i == 3:
        print('Ok, you know the rules. If you can\'t do it, I\'ll do it myself. The first coordinate of finish is 3')
        x2 = 3
        break
if x2 == x1+2 or x2 == x1-2 or x2 == x1+1 or x2 == x1-1:
    y2 = int(input('Please... input second coordinate of finish(1 - 8): '))
    i = 0
    while y2 > 8:
        y2 = int(input('Are you sure you can count? You know what is 8?: '))
        i += 1
        if i == 3:
            print(
                'Now I\'m not sure you can read either. Maybe you are a monkey in some science experiment?\n'
                'Ok, monkey, let\'s finish it anyway. The last coordinate of finish is 2')
            y2 = 2
            break
    if (x2 == x1+2 or x2 == x1-2) and (y2 == y1+1 or y2 == y1-1) or (x2 == x1+1 or x2 == x1-1) and (y2 == y1+2 or y2 == y1-2):
        print('That\'s right, knight can move like this. \nStart:', x1, ',', y1, '\nStart:', x2, ',', y2)
    else:
        print('Knight can\'t move like this')
else:
    print('Knight can\'t move like this')
