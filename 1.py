import datetime
today=datetime.date.today()
day=int(input("enter your date:"))
month=int(input("enter your month:"))
year=int(input("enter your year:"))
date1=datetime.date(year,month,day)
n_days=today-date1
print(n_days.days)

