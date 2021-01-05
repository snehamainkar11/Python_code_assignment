import calendar
from datetime import datetime
D = {'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':6,'2020-01-07':2,'2020-01-08':2}
totals = dict(zip(calendar.day_abbr, [0] * 7))
for date_str, value_str in D.items():
    totals[datetime.strptime(date_str, "%Y-%M-%d").strftime("%a")] += int(value_str)

print(totals)
