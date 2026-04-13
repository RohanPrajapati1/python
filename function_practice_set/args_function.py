#  *args functionn allows us to pass a variable number of argunments to a fucntion 
def sum(*args):
    # return sum(args)
    print(args) # args is a tuple
    print(*args) # unpacking the tuple
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum(1,2,3))
print(sum(1,2,3,4,5))