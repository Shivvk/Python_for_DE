# Function to replace all occurrences of a substring in a string
def replace_substring(main_string, old_substring, new_substring):
    return main_string.replace(old_substring, new_substring)

# Function to find the index of the first occurrence of a substring
def find_first_occurrence(main_string, substring):
    return main_string.find(substring)

# Function to capitalize the first letter of each word in a string
def capitalize_words(main_string):
    return main_string.title()

# Function to check if a string starts with a specific prefix
def check_prefix(main_string, prefix):
    return main_string.startswith(prefix)

# Main function to integrate all functionalities
def main():
    # Input string and required substrings/prefixes
    main_string = "hello, world! welcome to the world of python."
    old_substring = "world"
    new_substring = "Earth"
    substring_to_find = "welcome"
    prefix = "Hello"

    # Perform the operations
    updated_string = replace_substring(main_string, old_substring, new_substring)
    first_occurrence_index = find_first_occurrence(main_string, substring_to_find)
    capitalized_string = capitalize_words(main_string)
    does_start_with_prefix = check_prefix(main_string, prefix)

    # Display the results
    print(f"Original string: {main_string}")
    print(f"Updated string (replaced '{old_substring}' with '{new_substring}'): {updated_string}")
    print(f"First occurrence of '{substring_to_find}' is at index: {first_occurrence_index}")
    print(f"Capitalized string: {capitalized_string}")
    print(f"Does the string start with '{prefix}'? {does_start_with_prefix}")

