# Check if an amount can be evenly divided into 2000, 500, and 100 currency notes. 
amount = int(input("Enter the amount: "))
if amount % 2000 == 0:
    print("Amount can be divided into 2000 currency notes.")
elif amount % 500 == 0:
    print("Amount can be divided into 500 currency notes.")
elif amount % 100 == 0:
    print("Amount can be divided into 100 currency notes.")
else:
    print("Amount cannot be evenly divided into 2000, 500, or 100 currency notes.")
