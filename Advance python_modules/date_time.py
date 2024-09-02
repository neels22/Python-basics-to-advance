
import datetime

# from datetime import datetime

mytime  = datetime.time(13,20,1,20)

print(mytime.minute)
print(mytime.hour)
print(mytime.microsecond)
print(mytime)
print(type(mytime))


today = datetime.date.today()
print(today)
print(today.year)
print(today.month)
print(today.day)

print('\n')

print(today.ctime())

print('\n')

# mydatetime = datetime(2021,10,3,14,20,1)
# print(mydatetime)

##########################
from datetime import date

date1 = date(2021,11,3)
date2 = date(2022,11,3)

result = date2 - date1

print(result)
print(type(result))

###########################

from datetime import datetime

datetime1 = datetime(2021,11,3,22,0)
datetime2 = datetime(2023,11,3,12,0)

res = datetime1 - datetime2
print(res)
