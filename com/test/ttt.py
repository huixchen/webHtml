import datetime, time, calendar


def months(dt, months):  # 这里的months 参数传入的是正数表示往后 ，负数表示往前
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12+1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    dt = dt.replace(year=year, month=month, day=day)
    return dt


time_temp = '2015-02-28'
dt = datetime.date(int(time_temp[0:4]), int(time_temp[5:7]), int(time_temp[8:10]))
print('一个月前的今天是', months(dt, 1))
print('6个月前的今天是', months(dt, -6))