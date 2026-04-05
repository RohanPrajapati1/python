# while loop 
count = 0
while count < 5:
    print(count)
    count += 1
# else:
#     print("count is not less than 5")
# for loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
else:
    print("fruits are over")
# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# loop through a string
for x in "banana":
    print(x)
# break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# continue statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# range() function
for x in range(6):
    print(x)
# range() function with start parameter
for x in range(2, 6):
    print(x)
# range() function with start, stop and step parameter
for x in range(2, 30, 3):
    print(x)
# else in for loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# nested loop with else
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
else:
    print("Finally finished!")
# pass statement
for x in [0, 1, 2]:
    pass