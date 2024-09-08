def is_palindrome(input_string):
    # Loop through the first half of the string
    for i in range(0, len(input_string) // 2):
        # Compare the character at position 'i' from the start with the character at position 'i' from the end
        if input_string[i] != input_string[len(input_string) - i - 1]:
            # If any characters do not match, it's not a palindrome
            return "not palindrome"
    # If all character pairs match, it's a palindrome
    return "palindrome"

# Test with the example string
text1 = "racecar"
print(f"Version1: given string: {text1} is", is_palindrome(text1))

text2 = "RACEcar"
print(f"Version1: given string: {text2} is", is_palindrome(text2))
#---------------------------

#Version2
string = "madam"
print(f"Version2: Given string {string} is :", "palindrome" if string==string[::-1] else "not palindrome")
