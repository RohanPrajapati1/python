# Take a 3-digit number and check if all digits are distinct.
num = int(input("Enter 3 digit number: "))
rem = num % 10 
if num // 100 == rem :
    print("Digits are not distinct.")
elif num // 10 % 10 == rem:
    print("Digit are not distinct.")
else:
    print("Digits are distinct.")