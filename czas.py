import calendar as c
import time

import arrow

print(c.calendar(2022))
print(c.month(1983, 3))
print(c.firstweekday())

local_time = time.ctime()
print(local_time)

time_str = time.strftime("dziś jest %d, miesiąc to %m, roku %Y ")
time_str2 = time.strftime("mamy godzinę %H minut %M ")
# time.sleep(5)
print(time_str)
print(time_str2)

print(arrow.now())
print(arrow.now("Pacific/Pago_Pago"))


