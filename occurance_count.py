def occurrence(string, char):
    # Ensure the character is a single character
    if len(char) != 1:
        raise ValueError("The 'char' parameter should be a single character")

    # Count occurrences of the character in the string
    count_char = string.count(char)
    return count_char

# Test case 1
string = "Shivakiran"
char = "i"
print(f"The count of '{char}' in the given '{string}' is: {occurrence(string, char)}")

# Test case 2
string2 = "Shivakiran"
char2 = "x"
print(f"The count of '{char2}' in the given '{string2}' is: {occurrence(string2, char2)}")

# Test case 3 (will raise an error because char3 is not a single character)
string3 = "Shivakiran"
char3 = "iv"
try:
    print(f"The count of '{char3}' in the given '{string3}' is: {occurrence(string3, char3)}")
except ValueError as e:
    print(e)
