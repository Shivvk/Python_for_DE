def count_frequency(string):
    # Create an empty dictionary to store character frequencies
    frequency = {}

    # Iterate over each character in the string
    for char in string:
        # If the character is already in the dictionary, increment its count
        if char in frequency:
            frequency[char] += 1
        # Otherwise, add the character to the dictionary with a count of 1
        else:
            frequency[char] = 1

    return frequency


# Example usage
string = "data engineering"
result = count_frequency(string)

# Print the frequency of each character
for char, count in result.items():
    print(f"'{char}': {count}")
