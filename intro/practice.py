# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter another number: "))
# num4 = int(input("Enter another number: "))

# if(num1 > num2 and num1 > num3 and num1 > num4):
#     print(num1, "is the largest number.")
# elif(num2 > num1 and num2 > num3 and num2 > num4):
#     print(num2, "is the largest number.")   
# elif(num3 > num1 and num3 > num2 and num3 > num4):
#     print(num3, "is the largest number.")
# else:
#     print(num4, "is the largest number.")


# sub1 = int(input("Enter marks of the first subject: "))
# sub2 = int(input("Enter marks of the second subject: "))
# sub3 = int(input("Enter marks of the third subject: "))

# if(sub1 < 33 or sub2 < 33 or sub3 < 33):
#     print("You have failed in the exam.")
# elif(sub1 + sub2 + sub3)/3 < 40:
#     print("You have failed in the exam.")
# else:
#     print("Congratulations! You have passed the exam.")



# users = ["Harry " , "Rohan" , "Vivek" , "Shivanshu" , "Kaif" , "Shivam" , "Vridhi"]
# for x in users:
#     print("Hello" , x)


# num = int(input("Enter any number:"))
# print("The Table of given number is:")
# for i in range(1 ,11):
#     print(num , "X" , i , "=" , num*i)



# num = int(input("Enter any number:"))
# j = 0
# for i in range(1 , num):
#     if num % i == 0:
#         j += 1


# if j==2:
#     print(num , "is not a prime number.")
# else:   
#     print(num , "is a prime number.")


# n = 3
# for i in range(1 , n+1):
#     for j in range(1 , 4-i):
#         print(" " , end="")
#     for k in range(1 , 2*i):
#         print("*" , end="")
#     print()


# n1 = int(input("Enter a number: "))
# n2 = int(input("Enter another number: "))
# n3 = int(input("Enter another number: "))

# def largest(a , b ,c):
#     if(a > b):
#         if(a > c):
#             return a
#         else:
#             return c
        
#     elif b > c:
#         return b
#     else:
#         return c
    

# print(largest(n1 , n2 , n3))



# temp = int(input("Enter the temperature today in celsius: "))

# def temp_convert(c):
#     f = ((9/5) * c) + 32
#     return f

# print("The temperature in fahrenheit is: ", temp_convert(temp))


num = int(input("Enter a number: "))

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n -1)
    
print("The sum of first", num , "natural numbers is: ", sum(num))