grocries = ["milk", "bread", "cheese"]

item = input("Enter item to add")
if item not in grocries:
    grocries.append(item)

remove_item = input("Enter item to remove")
if remove_item in grocries:
    grocries.remove(remove_item)

print("Your grocery list is: " , grocries )