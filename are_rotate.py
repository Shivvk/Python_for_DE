def are_rotations(string1, string2):
    # Check if both strings are of the same length and not empty
    if len(string1) != len(string2):
        return False

    # Concatenate string1 with itself and check if string2 is a substring of it
    temp = string1 + string1
    return string2 in temp


# Example usage
string1 = "hello"
string2 = "lohel"

if are_rotations(string1, string2):
    print(f"{string1} and {string2} are rotations of each other.")
else:
    print(f"{string1} and {string2} are NOT rotations of each other.")
