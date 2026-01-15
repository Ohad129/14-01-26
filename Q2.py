i: int = 0
small: int = 99
big: int = 1
summ: int = 0
while i < 20:
    grade: int = int(input('enter grade:'))
    if 0 <= grade <= 100:
        i += 1
        summ += grade
        if grade < small:
            small = grade
        if grade > big:
            big = grade
    else:
        print('invalid grade, enter again')
print('lowest grade is:', small)
print('highest grade is:', big)

print('the average grade is:', summ // i)

