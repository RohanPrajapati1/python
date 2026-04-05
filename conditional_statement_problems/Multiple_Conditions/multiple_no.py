# Check if one of two given numbers is a multiple of the other.
num1 = int(input("Enter any positive number: "))
num2 = int(input("Enter another positive number: "))

if num1 % num2 == 0:
    print(f"{num2} is multiple of {num1}")
elif num2 % num1 == 0:
    print(f"{num1} is multiple of {num2}")
else:
    print(f"{num1} and {num2} are not multiple of each other.")