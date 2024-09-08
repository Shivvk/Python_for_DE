# Function to convert string to uppercase and lowercase
def convert_case(string):
    uppercase = string.upper()
    lowercase = string.lower()
    return uppercase, lowercase

# Function to replace all occurrences of a substring
def replace_substring(original_string, old_substring, new_substring):
    updated_string = original_string.replace(old_substring, new_substring)
    return updated_string

# Example usage
string = "Hello, Python World! Welcome to the world of Python."

# Convert string to uppercase and lowercase
uppercase_string, lowercase_string = convert_case(string)
print(f"Original String: {string}")
print(f"Uppercase: {uppercase_string}")
print(f"Lowercase: {lowercase_string}")

# Replace all occurrences of a substring
old_substring = "Python"
new_substring = "Data Engineering"
updated_string = replace_substring(string, old_substring, new_substring)
print(f"Updated String: {updated_string}")
