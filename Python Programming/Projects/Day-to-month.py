days = int(input("Enter the number of days: "))

month = days//30
day=days%30

if day > 0:
    print(f"{month} month(s) and {day} day(s)")
else:
    print(f"{month} month(s)")