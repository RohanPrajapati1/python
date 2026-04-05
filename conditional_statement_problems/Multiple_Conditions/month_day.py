#  Take a month number (1–12) and print the number of days in that month (ignore leap years)
month = int(input("Enter month (1-12): "))

if 1 <= month <= 12:
    if month in [1,3,5,7,8,10,12]:
        print("This month has 31 days")
    elif month in [4,6,9,11]:
        print("This month has 30 days")
    else:
        print("This month has 28 days")
else:
    print("Invalid month number.")