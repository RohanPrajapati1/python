# Check whether a given integer is single-digit, double-digit, or multi-digit.
num = int(input("Enter a number: "))
if num // 10 == 0:
    print("Number is single digit.")
elif num // 100 == 0:
    print("Number is double digit.")
else:
    print("Number is multi-digit.")
