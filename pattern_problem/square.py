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


for i in range(1 , 6):
    print(" " * (5 - i) , "* " * i)

num = 1
for i in range(1 , 8):
    for j in range(0, i):
        print(num , end=" ")
        if(num == 9):
            num = 0
        else:
            num += 1
    print()



for i in range(1, 6):
    for j in range(0 , i):
        print((i + j) % 2 , end=" ")
    print()


num = 65
for i in range(0 , 5):
    for j in range(0 , i + 1):
        print(chr(num) , end=" ")
        num += 1
    print()


num = 65
for i in range(0 , 5):
    for j in range(0 , i + 1):
        print(chr(num) , end=" ")        
    num += 1   
    print()


num = 65
for i in range(0 , 5):
    for j in range(0 , i + 1):
        print(chr(num + j) , end=" ")
    print()


num = 65
for i in range(1 , 6):
    print(" " * (5 - i) , end="")
    for j in range(0 ,2*i - 1):
        print(chr(num) , end="")
        num += 1
    print()

# pascal's triangle
num = 1
for i in range(1,6):
    print(" " * (5 - i) , end="")
    for j in range(1 , i + 1):
        print(j , end="")
    for k in range(i - 1 , 0 , -1):
        print(k , end="")
    print()


for i in range(1 , 6):
    print("*" * i)
for j in range(4 , 0 , -1):
    print("*" * j)


for i in range(1 , 6):
    print("*" * i)
for j in range(5 , 0 , -1):
    print("*" * j)



for i in range(1 , 6):
    print(" " * (5 - i) , "*" * (2*i - 1))
for i in range(4 , 0 , -1):
    print(" " * (5 - i) , "*" * (2*i - 1))

