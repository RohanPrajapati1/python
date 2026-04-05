balance = 77000.00
withdrawal_amount =float(input("Enter the amount to withdraw: "))

if withdrawal_amount > balance:
    print("Insufficient amount in the account.")
else:
    balance -= withdrawal_amount
    print("withdrawal successful")

