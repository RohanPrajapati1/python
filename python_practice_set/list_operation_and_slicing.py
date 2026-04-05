# even number in a list 
def even_numbers(list):
    return [num for num in list if num % 2 == 0]
# explanation of return statement:
# This list comprehension iterates through each number in the input list,
# checking if it is even (i.e., if the number modulo 2 equals 0).
# If the condition is true, the number is included in the new list.

print(even_numbers([1, 2, 3, 4, 5, 6]))  # [2, 4, 6]



#Maximum and minimum numbers in a list
def max_min_numbers(list):
    max = list[0]
    min = list[0]

    for i in list :
        if i >= max:
            max = i
        if i <= min:
            min = i
    return {"max" : max , "min" : min}

print(max_min_numbers([1, 2, 3, 4, 5, 6]))  # {'max': 6, 'min': 1}



# Reverse a list
def reverse_list(list):
    return list[: : -1]

print(reverse_list([1, 2, 3, 4, 5, 6]))  # [6, 5, 4, 3, 2, 1]




# remove duplicates from a list
def remove_duplicates(listS):
    return list(set(listS))
print(remove_duplicates([1, 2, 3, 4, 5, 6, 1, 2, 3]))  # [1, 2, 3, 4, 5, 6]



# rotate a list
def rotate_list(list, n):
    n = n % len(list)  # Handle cases where n is larger than the list length
    return list[-n:] + list[:-n]
print(rotate_list([1, 2, 3, 4, 5, 6], 2))  # [5, 6, 1, 2, 3, 4]



# Count occurrences of an element in a list
def count_occurrences(list, element):
    return list.count(element)
print(count_occurrences([1, 2, 3, 4, 5, 6, 1, 2, 3], 1))  # 2




# sort a list in ascending order and descending order
def sort_list_ascending(list):
    return sorted(list)
def sort_list_descending(list):
    return sorted(list, reverse=True)
print(sort_list_ascending([6, 5, 4, 3, 2, 1]))  # [1, 2, 3, 4, 5, 6]
print(sort_list_descending([1, 2, 3, 4, 5, 6]))  # [6, 5, 4, 3, 2, 1]


#itration of list using []
#1.
#[: : -1] is used to reverse a list in Python.
##2.
#list[::2] is used to get every second element from a list in Python.
#3.
#list[1::2] is used to get every second element from a list starting from the second element in Python.
#4.
#list[1:5] is used to get elements from index 1 to index 4 (not including index 5) in a list in Python.
#5.
#list[1:5:2] is used to get every second element from index 1 to index 4 (not including index 5) in a list in Python.
#6.
#list[-1] is used to get the last element of a list in Python.
#7.
#list[-2] is used to get the second last element of a list in Python.
#8.
#list[-3:] is used to get the last three elements of a list in Python.
#9.
#list[:-3] is used to get all elements of a list except the last three elements in Python.
