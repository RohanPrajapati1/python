a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

hcf = 1
lcm = max(a , b)

# loop for hcf
for i in range(1, min(a,b) + 1):
    if a % i == 0 and b % i == 0:
        hcf = i

# loop for lcm
while True:
    if lcm % a == 0 and lcm % b == 0:
        break
    lcm += 1

print("LCM of", a, "and", b, "is:", lcm)
print("HCf of", a, "and", b, "is:", hcf)