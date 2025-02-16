from datetime import datetime, time
def date_diff_in_Seconds(d2, d1):
    timedelta = d2 - d1
    return timedelta.days * 24 * 3600 + timedelta.seconds
date1 = datetime.strptime('2022-03-01 01:00:00', '%Y-%m-%d %H:%M:%S' )
date2 = datetime.now()
print(date_diff_in_Seconds(date2, date1))