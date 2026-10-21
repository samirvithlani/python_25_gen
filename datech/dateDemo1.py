import datetime

print(datetime.datetime.now()) #date time 
print(datetime.date.today()) #date

d = datetime.date(2025,2,14)
t = datetime.time(14,2,25)

print(d)
print(t)


dt = datetime.datetime(2007,7,7,7,7,7)
print(dt)

now = datetime.datetime.now()

print("Year",now.year)
print("month",now.month)
print("day",now.day)

#format

#data to string..
print(now.strftime("%d-%m/%Y"))
print(now.strftime("%d-%m-%y"))
print(now.strftime("%d-%b-%y")) 
print(now.strftime("%A"))
print(now.strftime("%a"))
print(now.strftime("%B"))
print(now.strftime("%H"))
print(now.strftime("%I"))
print(now.strftime("%S"))
print(now.strftime("%p"))

#string -->date
date_str = "25-12-26"

d = datetime.datetime.strptime(date_str,"%d-%m-%y")
print(d)



today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(hours=10)
next_day = today + datetime.timedelta(days=2)
next_week = today + datetime.timedelta(weeks=1,days=1)

print(tomorrow)
print(next_day)
print(next_week)

now = datetime.datetime.now()
next_hr = now+datetime.timedelta(hours=1)
print(next_hr)


today = datetime.datetime.today()
tomorrow = today + datetime.timedelta(days=1)

diff  =  tomorrow -today
print(diff.days)


print(today<tomorrow)
print(today==tomorrow)
print(today>tomorrow)