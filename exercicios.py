
#Ex. 1
first_name = "Evineldy"
last_name = "Nharreluga" 
full_name = "Evineldy Antonio Nharreluga"
country = "Mozambique"
city = "Maputo"
age = 21
year = 2004
is_married = "no"
is_true = True
is_light_on = False
first_name, last_name, country, age, is_married = "Evineldy", "Nharreluga", "Mozambique", 21, False

#print(first_name, last_name, country, age, is_married)

'''print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(is_married))'''

'''import math 
#print(len(last_name) == len(first_name))
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = (num_one)^(num_two)
floor_division = num_one // num_two
area_circle = math.pi * float((30)^(2))
circum_of_circle = 2 * math.pi * 30

radius = int(input("Input Radius of the circle: "))
area_circle = math.pi * float((radius)^2)

first_name = str(input("First name: "))
last_name = str(input("Last name: "))
country = str(input("Country: "))
age = int(input("Age: "))
print(f"=============\nPERSONAL DATA: \nFirst Name: {first_name}\nLast Name: {last_name}\nCountry: {country}\nAge: {age}\n=============")
'''

#Exercises - Operators

'''b = float(input("Enter base: "))
h = float(input("Enter height: "))
area = 0.5 * b * h
print(f"The area of the triangle is {area}.")'''

'''a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
perimeter = a + b + c
print(f"The perimeter of the triangle is {perimeter}.")'''

'''l = float(input("Enter length: "))
w = float(input("Enter width: "))
area = l * w
perimeter = 2*(l + w)
print(f"The rectangle area is {area}m and its perimeter {perimeter}m.")
'''

'''import math
r = float("Input radius: ")
area = math.pi * r**2
c = 2 * math.pi * r
print(f"The circle area is {area} and its circumference {c}")'''

y_int = 2
m1 = 2
 #y=2x-2
x_int = y_int / m1
print(f"Slope is: {m1}")
print(f"x-intercept is ({x_int}, 0)")
print(f"y-intercept is (0, {y_int})")

import math
#Slope : m = (y2-y1)/(x2-x1)
#Euclidean distance : d = ((x2-x1)**2 + (y2-y1)**2)**(1/2)
#Points: (2,2) and (6,10)
x1 = 2
x2 = 3
y1 = 6
y2 = 10
m2 = (y2-y1) / (x2-x1)
d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print(f"Scope is {m2}\nEuclidean distance is: {d}")

print(m1 == m2)


#x^2 + 6x + 9 = 0
a = 1
b = 6
c = 9
d = b**2 - 4*a*c
x1 = (-b + math.sqrt(d))/2*a
x2 = (-b - math.sqrt(d))/2*a
print(f"x1 equals to {x1} and x2 equals to {x2}")

a = "python"
b = "dragon"
print(len(a) >= len(b))

if "on" in "python" and "dragon" :
    print(True)
else:
    print(False)

if "jargon" in "I hope this course is not full of jargon":
    print(True)

print(int(float(len("python"))))

x = int(input("Enter a number: "))
if x % 2 == 0:
    print("Even")
else:
    print("Not Even")

print(int(9.8) == 10)


'''hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
pay_person = hours * rate_per_hour
print(f"Your weekly earning is {pay_person}.")'''

num_years = int(input('Enter number of years you have lived: '))
minute = 60
hour = 60 * minute
day = 24 * hour
year = 365 * day
num_seconds = year * num_years
print(num_seconds)


print("1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125")