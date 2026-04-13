num = int(input("Enter a number: "))

fac = 1 
if num == 0:
    print("The factorial is: " , fac)
while num > 0:
    fac *= num
    num -= 1

print("The factorial is: " , fac)
