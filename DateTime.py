import datetime

# NOTE: time
t = datetime.time(5, 25, 1)     # hour : minute : second : microsecond : timezone
print(t)

print t.min
print t.max
print t.resolution        # micro second

# NOTE: date
today = datetime.date.today()
print today
today.timetuple()
today.day
today.month
today.year

print datetime.date.min
print datetime.date.max
print datetime.date.resolution

d1 = datetime.date(2018, 3, 11)       # year : month : day
print d1

d2 = d1.replace(year=1990)
print d1
print d2

(d1 - d2).__str__()
