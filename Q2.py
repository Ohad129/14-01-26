#        קלוט 20 ציונים מהמשתמש
#       אם הציון נמוך מ־0 או גדול מ־100 התעלם מהציון והמשך לקלוט
#      עד שתקבל 20 ציונים חוקיים
#     הדפס את הציון הכי גבוה
#    הדפס את הציון הכי נמוך
#   הדפס את ממוצע הציונים

i: int = 0
small: int = 50
big: int = 50
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