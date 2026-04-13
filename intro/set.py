# set are used to store multiple item in a single variable
# set is immutalble , unordered and un indexed 
# set item are unchangeable but we can remove and add item 
# do not allow duplicate values

set = {1 ,3,5,7,2 ,3,4,3,3,3}
print(set) # {1, 2, 3, 4, 5, 7} duplicate value are removed

# accessing item in set
for item in set:
    print(item)

# add item
set.add(6)
print(set) # {1, 2, 3, 4, 5, 6, 7}

set2 = {8,9,10} # this can be list or tuple also (meaans iterable)

set.update(set2)
print(set) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# removing item
# 1. remove() - removes the specified item, if the item does not exist, it raises a KeyError
set.remove(10)

# 2. discard() - removes the specified item, if the item does not exist, it does not raise a KeyError
set.discard(11)

# join set
set3 = {11,12,13}
set4 = set.union(set3) # returns a new set that contains all the items from
# both sets, excluding duplicates
print(set4) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}
set5 = set.intersection(set3) # returns a new set that contains only the items that are present in both sets
print(set5) # set() empty set because there is no common item in both sets
set6 = set.difference(set3) # returns a new set that contains only the items that are present in the first set but not in the second set
print(set6) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set7 = set.symmetric_difference(set3) # returns a new set that contains only the items that are present in either set, but not in both sets
print(set7) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13} because there is no common item in both sets
