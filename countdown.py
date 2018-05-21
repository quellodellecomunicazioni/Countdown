from datetime import datetime
from dateutil import relativedelta
import time

# today May 20, 2018, 16:58
today = datetime.today()

# deadline Jun 14, 2018, 12:10
y = 2018
m = 8
d = 16
h = 15
min = 10
s = 0
ddline = datetime(y, m, d, h, min, s)

difference = relativedelta.relativedelta(ddline, today)
years = difference.years
months = difference.months
days = difference.days
hours = difference.hours
minutes = difference.minutes
seconds = difference.seconds
when_to_stop = int((ddline - today).total_seconds())

while True:
    while when_to_stop > 0:
        m, s = divmod(when_to_stop, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        time_left = str(d).zfill(2) + ":" + str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print(time_left + "\r", end="")
        time.sleep(1)
        when_to_stop -= 1
