from datetime import datetime

now = datetime.now()
print(now)
t = now.strftime('%m/%d/%Y, %H:%M:%S')
print(t)

from datetime import date
string_today = '5 December, 2019'
string_object = datetime.strptime(string_today, '%d %B, %Y')

today = date(year=2026, month=2, day=17)
new_year = date(year=2027, month=1, day=1)
print(new_year-today)

then = date(year=1970, month=1, day=1)
print(today-then)