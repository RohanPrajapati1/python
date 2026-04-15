# square of stars
for i in range(1 , 6):
    print("*" * 5)


# triangle 
for i in range(1 , 6):
    print("*" * i)


# right aligned triangle
for i in range(1 , 6):
    print(" " * (6 - i) ,  "*" * i)


# Print Stars in Even Numbers (2, 4, 6, 8, 10)
for i in range(2 , 11 , 2):
    print("*" * i)


# centered pyramid
for i in range(0 , 5):
    print(" " * (5 - i - 1) , "*" * (2 * i + 1))


# Print Numbers in an Increasing Sequence (1, 12, 123, 1234, 12345)
for i in range(1 , 6):
    for j in range(1 , i+1):
        print(j , end="")
    print()


# Print Repeated Numbers per Row (Same Number Repeated)
for i in range(1 , 6):
    for j in range(1 , i+1):
        print(i , end="")
    print()

num = 1
for i in range(1 , 6):
    for j in range(1 , i + 1):
        print(num , end=" ")
        num += 1
    print()
