# Check if a number lies within the range [100, 999].
num = int(input("Enter a number: "))

# 1 approach 
if 100 <= num <= 999:
    print("The number lies between 100 and 999.")
else:
    print("The number does not lie between 100 and 999.")

# 2 approach
if num in range(100 , 1000):
    print("The number lies between 100 and 999.")
else:
    print("The number does not lie between 100 and 999.")

# 3 approach
if len(str(num)) == 3:
    print("The number lies between 100 and 999.")
else:
    print("The number does not lie between 100 and 999.")