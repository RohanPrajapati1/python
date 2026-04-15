# Take an integer (1–9999) and check if the sum of its digits is greater than the product 
# of its digits. 
num = int(input("Enter number between (1-9999): "))
sum_digits = 0
product_digits = 1
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum_digits += digit
    product_digits *= digit
    temp_num //= 10

if sum_digits > product_digits:
    print("Sum of digits is greater than product of digits.")
elif sum_digits < product_digits:
    print("Product of digits is greater than sum of digits.")
else:
    print("Sum and product of digits are equal.")
