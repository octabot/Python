import datetime as dt

date = dt.date(2026, 11, 7)   #date
print(date)

today = dt.date.today()    #today's date
print(today)

time = dt.time(21,21,21)   #time
print(time)

now = dt.datetime.now()    #current time with date
print(now)

nows = now.strftime("%H:%M:%S %d-%m-%y")
print(nows)