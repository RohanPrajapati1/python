str = input("Enter a string: ")
rev_str = ""

for i in range(len(str) -1 , -1 , -1):
    rev_str += str[i]

print("Reversed string: " , rev_str)