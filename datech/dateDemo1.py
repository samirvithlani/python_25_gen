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
print(now.strftime("%d-%b-%y")) #doubt
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
