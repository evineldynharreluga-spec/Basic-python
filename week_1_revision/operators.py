age = int(22)
height = float(1.72)
complex_number = 1+6j
''''base = int(input('Enter base: '))
height = int(input('Enter height: '))'''
#area = 0.5 * base * height
#print(f'The area of the triangle is {area}')

#Formula: y = slope * x -2
x = 0
y = 0
slope = 2
print(f'y_intercept is {slope * x - 2}')
print(f'x_intercept is {slope  / 2}')
x1 = 2 
y1 = 2
x2 = 6
y2 = 10
m = (y2 - y1)/(x2 - x1)

import math

euclidean_distance = math.sqrt((x2 - x1)**2 + (y2-y1)**2)

print(euclidean_distance == math.sqrt(80))

#y = x**2 + 6x + 9
a = 1
b = 6
c = 9
delta = b**2 - 4 * a * c
x12 = (-b - math.sqrt(delta))/2 * a
print(x12)
print(math.sqrt(0))

