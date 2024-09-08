#Version1 : without using slicing
def reverse_string_loop(input_string):
    # Initialize an empty string to store the reversed string
    reversed_string = ""
    # Iterate through each character in the input string
    for char in input_string:
        # Prepend each character to the reversed string
        reversed_string = char + reversed_string
    return reversed_string

# Test the function
text = "Python"
print(f"Reversed string (using loop): {reverse_string_loop(text)}")

#version2 : using slicing
string = "Shivakiran"
print (f"the reverse of given string {string} is : ", string[::-1])


#version3:

def reverse_string_reversed(input_string):
    # Use the reversed() function and join() to reverse the string
    return ''.join(reversed(input_string))

# Test the function
text = "Python"
print(f"Reversed string (using reversed and join): {reverse_string_reversed(text)}")

