# Take a character and check if it’s a vowel or consonant.
char = input("Enter a character: ")
vowels = "AEIOUaeiou"
if char in vowels:
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")