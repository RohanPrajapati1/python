# Check if a number is a multiple of 7 or ends with 7.
num = int(input("Enter a number: "))

if num % 7 == 0:
    print(f"{num} is a multiple of 7.")
elif num % 10 == 7:
    print(f"{num} ends with 7.")
else:
    print(f"{num} neither  multiple of 7 nor ends with 7.")