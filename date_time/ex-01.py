from datetime import datetime

''''now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now. second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')'''

#Formatacoes usando strftime

''''new_year = datetime(2026, 1, 1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(f'{day}/{month}/{year}, {hour}:{minute}:{second}')

now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time: ',t)
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print('time one: ', time_one)
time_two = now.strftime('%d/%m/%Y, %H:%M:%S')
print(time_two)'''

''''date_string = '5 December, 2019'
print('date_string =', date_string)
date_object = datetime.strptime(date_string, '%d %B, %Y')
print('date_object =', date_object)
'''

from datetime import date
d = date(2020, 1, 1)
print(d)
print(d.today())
today = d.today()
day = today.day
print(day)

from datetime import date, datetime


today = date(year=2026, month=2, day=17)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)



