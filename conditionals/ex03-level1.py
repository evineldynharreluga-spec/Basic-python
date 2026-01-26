n1 = int(input('Enter number one: '))
n2 = int(input('Enter number two: '))

if n1 > n2:
    print(f'{n1} is greater than {n2}')
elif n1 < n2:
    print(f'{n2} is greater than {n1}')
else:
    print(f'{n1} is equal to {n2}')