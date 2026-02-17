import datetime

''''from datetime import datetime
now = datetime.now()
print(now)
day = now.day
print(day)
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')
'''

from datetime import datetime
new_year = datetime(2020, 1, 1)
print(new_year)
day = new_year.day
print(day)

now = datetime.now()
t = now.strftime('%H:%M:%S')
print('time:',t)
time_one = now.strftime('%m/%d/%Y, %H:%M:%S')
print(time_one)