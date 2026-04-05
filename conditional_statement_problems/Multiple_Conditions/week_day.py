weekDay = {1 : "Monday", 2 : "Tuesday", 3 : "Wednesday", 4 : "Thursday", 5 : "Friday", 6 : "Saturday", 7 : "Sunday"}

day = int(input("Enter a number between 1 to 7: "))

if 1 <= day <= 7:
    print(f"The day is {weekDay[day]}")
else:
    print("Invalid input!.")
