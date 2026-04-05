#  Check whether a number is a perfect square (without using the square root function).
num = int(input("Enter a number: "))
is_perfect_square = False
if num == 1:
    is_perfect_square = True
else:
    for i in range( 1 , num // 2 + 1):
        if i * i == num:
            is_perfect_square = True
            break

if is_perfect_square:
    print(num , " is a perfect square.")
else:
    print(num, " is not a perfect square.")