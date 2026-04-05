# Take an alphabet character and check if it lies between ‘a’ and ‘m’ or ‘n’ and ‘z’.

char = input("Enter an alphabet: ")

if 'a' <= char.lower() <= 'm':
    print(f"{char} lie beteween 'a' and 'm'." )
else:
    print(f"{char} lie between 'n' and 'z'.")
