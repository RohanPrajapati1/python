# Print all numbers from 1–n whose binary representation has an even number of 1s. 

# 1. approach

def by_using_build_in_function(n):
    result =  []
    for i in range(1 , n + 1):
         if bin(i).count('1') % 2 == 0:
            result.append(i)
    return result

print(by_using_build_in_function(20))
