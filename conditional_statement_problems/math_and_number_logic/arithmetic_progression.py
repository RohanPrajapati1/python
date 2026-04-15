# Take three numbers and check if they are in arithmetic progression.
print("Enter three numbers in increasing order: ")
num1 = int(input("1. "))
num2 = int(input("2. "))
num3 = int(input("3. "))
if num1 == num2 | num1 == num3 | num2 == num3:
    print("Numbers are not in arithmetic progression")
else:
    if  num2 - num1 == num3 - num2:
        print("Numbers are in arithmetic progression.")
    else:
        print("Numbers are not in arithmetic progression")

        