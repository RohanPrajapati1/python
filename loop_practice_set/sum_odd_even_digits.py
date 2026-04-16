# Print the sum of all odd digits and even digits separately in a number.

num = int(input("Enter any larger number: "))
odd_sum = 0
even_sum = 0
while num > 0:
    rem = num % 10
    if rem % 2 == 0:
        even_sum += rem
    else:
        odd_sum += rem
    num //= 10

print(f"Sum of odd digits is {odd_sum} , sum of even digits is {even_sum}")