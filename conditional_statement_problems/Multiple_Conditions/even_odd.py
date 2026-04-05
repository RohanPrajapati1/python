num1 = int(input("Enter any positive number: "))
num2 = int(input("Enter another positive number: "))

if num1 % 2 == 0 :
    if num2 % 2 == 0:
        print("Both are even.")
    else:
        print("First is even and second is odd.")
elif num2 % 2 == 0:
    print("First is odd and second is even.")
else:
    print("Both are odd.")