# Frequency of a each character in a string
def frequency_of_char(string):
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char , 0) + 1
    return frequency

print(frequency_of_char("hello world"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}



# check if a string is a palindrome
def is_palindrome(string):
    if string == string[: : -1]:
        return True
    else:
        return False   
    
print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False




# count the number of vowels , consonent , digits and special characters in a string
def count_vowels_consonants_digits_special(string):
    vowels = "aeiouAEIOU"
    consonants ="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    digits = "0123456789"
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    special_characters_count = 0

    for i in string:
        if i in vowels:
            vowels_count += 1
        elif i in consonants:
            consonants_count += 1
        elif i in digits:
            digits_count += 1
        else:
            special_characters_count += 1
    return {
        "vowels": vowels_count,
        "consonants": consonants_count,
        "digits": digits_count,
        "special_characters": special_characters_count
    }
print(count_vowels_consonants_digits_special("Hello World! 123"))
# {'vowels': 3, 'consonants': 7, 'digits': 3, 'special_characters': 2}



# reverse a string
def reverse_string(string):
    return string[::-1]
print(reverse_string("hello"))  # "olleh"



#remove all spaces from a string
def remove_spaces(string):
    return string.replace(" ", "")
print(remove_spaces("hello world"))  # "helloworld"



#replace all occurrences of a substring in a string
def replace_substring(string, old, new):
    return string.replace(old, new)
print(replace_substring("hello world", "world", "Python"))  # "hello Python"



# check if a string is an anagram of another string
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))  # True
#anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



def capatalise_first_letter(string):
    return string.capitalize()
print(capatalise_first_letter("hello world"))  # "Hello world"




# capitalize the first letter of each word in a string
def capitalize_first_letter_of_each_word(string):
    return string.title()   
print(capitalize_first_letter_of_each_word("hello world"))  # "Hello World"


# occurrence of each word in a string
def word_frequency(string):
    words = string.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
print(word_frequency("hello world hello"))  # {'hello': 2, 'world': 1}



