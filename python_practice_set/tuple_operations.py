## Function to find the sum of all elements in a tuple
# Tuple Operations
def summ_of_elements(tup):
    return sum(tup)

print(summ_of_elements((1, 2, 3, 4, 5)))  # Output: 15



# how many elements are greater than a given number in a tuple
def count_greater_than(tup, number):
    return sum(1 for x in tup if x > number)
print(count_greater_than((1, 2, 3, 4, 5), 3))  # Output: 2



# convert a tuple to a list add an element and convert it back to a tuple
def add_element_to_tuple(tup, element):
    temp_list = list(tup)  # Convert tuple to list
    temp_list.append(element)  # Add element to the list
    return tuple(temp_list)  # Convert back to tuple
print(add_element_to_tuple((1, 2, 3), 4))  # Output: (1, 2, 3, 4)
