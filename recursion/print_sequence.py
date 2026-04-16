def print_reverse_sequence(n):
    if n == 1:
        print('1' , end=" ")
        return
    print(n , end=" ")
    return print_reverse_sequence(n - 1)

def print_sequence(start , n):
    if start == n:
        print(n , end=" ")
        return
    print(start , end=' ')
    return print_sequence(start + 1 , n)

def print_even_sequence(start , n):
    if start == n and n % 2 == 0:
        print(n , end=" ")
        return
    elif start == n:
        return
    print(start , end=" ")
    return print_even_sequence(start + 2 , n)

def sum_n_number(n):
    if n == 1:
        return 1
    return n + sum_n_number(n - 1)

def power_of_number(x , n):
    if n == 1:
        return x
    return x * power_of_number(x , n - 1)

def digit_sum(n):
    if n == 0:
        return 0
    return (n % 10) + digit_sum(n//10)





print_reverse_sequence(10)
print()
print_sequence(1 , 10)
print()
print_even_sequence(2 , 20)
print()
print(sum_n_number(6))
print(power_of_number(2,3))
print(digit_sum(123))
