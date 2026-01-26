score = int(input('Enter your grade: '))
if score>=90 and score<=100:
    print('GRADE: A')
elif score>=80 and score<=89:
    print('GRADE: B')
elif score>=70 and score<=79:
    print('GRADE: C')
elif score>=60 and score<=69:
    print('GRADE: D')
else:
    print('GRADE: F')