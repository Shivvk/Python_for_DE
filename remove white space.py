# Method 1: Using replace()
def remove_space(string):
    # Replace all spaces with an empty string
    word = string.replace(" ", "")
    print(word)

# Test the function
string = "python is easy to learn"
remove_space(string)

# Method 2: Using List Comprehension
def text_space(string):
    # Join characters that are not spaces
    return "".join([char for char in string if not char.isspace()])

# Test the function
text = "Python is easy to learn"
print(f"Original string: '{text}'")
print(f"String without whitespaces: '{text_space(text)}'")

# Method 3: Using split() and join()
def remove_whitespaces(input_string):
    # Split the string into words and join them without spaces
    return "".join(input_string.split())

# Test the function
text = "Python is very easy to learn"
print(f"Original string: '{text}'")
print(f"String without whitespaces: '{remove_whitespaces(text)}'")
