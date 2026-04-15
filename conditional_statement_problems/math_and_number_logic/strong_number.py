# Check if a number is a strong number (sum of factorials of digits = number). 
# eg: 145 is a strong number because 1!+ 4!+ 5!=1 + 24 + 120 = 145 which equals the original number

num = int(input("Enter any positive number: "))
temp_num = num
fact_sum = 0

def factorial(num):
    if num == 0 or num == 1:
        return 1 
    return num * factorial(num - 1)

while temp_num > 0:
    single_digit = temp_num % 10
    fact_sum += factorial(single_digit)
    # print(f"{fact_sum}")
    temp_num //= 10

if fact_sum == num:
    print("Number is strong number.")
else:
     print("Number is not a strong number.")