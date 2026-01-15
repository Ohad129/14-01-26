a: int = int(input('enter a number'))
minn: int = a
if minn == 0:
    print('empty group')
else:
    while a != 0:
        if minn > a:
            minn = a
        a = int(input('enter new number'))
    print(minn)