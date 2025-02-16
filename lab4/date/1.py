from datetime import date, timedelta
today = date.today()
print("Today: ", today)
t = timedelta(5)
print("New: ", today - t)
