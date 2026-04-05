# Take a 3-digit number and determine if the middle digit is the largest, smallest, or neither. 
num = int(input("Enter a 3-digit number: "))
firstDigit = num // 100
lastDigit= num % 10
middleDigit = (num // 10) % 10

if middleDigit > firstDigit and middleDigit > lastDigit:
    print("The middle digit is the largest.")
elif middleDigit < firstDigit and middleDigit < lastDigit:
    print("The middle digit is the smallest.")
else: 
    print("The middle digit is neither largest nor smallest.")