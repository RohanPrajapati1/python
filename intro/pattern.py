n = 5 
m = 5
for i in range(1, n+1):
    for j in range(1, i):
        print("*" , end="")
    print()
# Output:
# 1 2 3 4 5
print()

# 1.
for i in range(6):
    for j in range(6):
        print("*" , end="")
    print()

print()


# 2.
for i in range(1 , 5):
    for j in range(1,5):
       if ( (i==2 and (j > 1 and j <4)) or (i==3 and (j >1 and j< 4))):
           print(" " , end="")
       else:
           print("*" , end="")           
    print() 

print() 

    # 3.
for i in range(1 , 5):
    for j in range(1 , i):
         print(" " , end="")
    for k in range(1 , 5):
        print("*" , end="")
    print() 

print() 

# 4.
for i in range(1 ,5):
    for j in range(1 , 5-i):
        print(" " , end="")
    for k in range(1 , 5):
        print("*" , end="")
    print()

print()

# 5.
        #       *
        #      ***
        #     *****
        #    *******
for i in range(1 , 5):
    for j in range(1 , 5-i):
        print(" " , end="")
    for k in range(1 , 2*i):
         if ( (i==2 and (k > 1 and k < 2*i -1)) or (i==3 and (k > 1 and k < 2*i -1))):
           print(" " , end="")
           # end is used to avoid new line after printing space
         else:
           print("*" , end="")  
    print()

print()

# 6.
