
x1 = int(input('Input first coordinate of start (1 - 8): '))
y1 = int(input('Input second coordinate of start (1 - 8): '))
x2 = int(input('Input first coordinate of finish (1 - 8): '))
if x2 == x1+2 or x2 == x1-2 or x2 == x1+1 or x2 == x1-1:
    y2 = int(input('Input second coordinate of finish(1 - 8): '))
    if (x2 == x1+2 or x2 == x1-2) and (y2 == y1+1 or y2 == y1-1) or (x2 == x1+1 or x2 == x1-1) and (y2 == y1+2 or y2 == y1-2):
        print('That\'s right, knight can move like this.')
    else:
        print('Knight can\'t move like this')
else:
    print('Knight can\'t move like this')


