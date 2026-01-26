my_age = 21
your_age = int(input('Enter your age: '))
if your_age > my_age:
    if (your_age - my_age) == 1:
        print(f'You are {your_age - my_age} year older than me')
    else:
        print(f'You are {your_age - my_age} years older than me')
elif your_age < my_age:
    if (my_age - your_age) == 1:
        print(f'I am {my_age - your_age} year older than you')
    else:
        print(f'I am {my_age - your_age} years older than you')
else:
    print('Yayyy! We have the same age!')