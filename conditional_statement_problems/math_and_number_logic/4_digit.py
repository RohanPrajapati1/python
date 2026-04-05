# Take a number and check if the first and last digits are equal.
num = int(input("Enter any number greater than 9: "))

lastDigit = num % 10
firstDigit = num 
while num > 0 :
    firstDigit = num % 10
    num = num // 10

if firstDigit == lastDigit:
    print("First and last digits are equal.")
else:
    print("First and last digits are not equal.")