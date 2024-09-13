def remove_duplicates(string):
    result = ""
    seen = set()

    for char in string:
        if char not in seen:
            result += char
            seen.add(char)

    return result

# Example usage
string = "programming"
result = remove_duplicates(string)
print("String after removing duplicates:", result)
