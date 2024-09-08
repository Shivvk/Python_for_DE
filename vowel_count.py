# Version 1: Counting vowels and consonants using a loop
def check_count(input_string):
    # Initialize counters for vowels and consonants
    vowel_count = 0
    constant_count = 0
    # Define vowels (both uppercase and lowercase)
    vowel = "aeiouAEIOU"

    # Iterate through each character in the string
    for char in input_string:
        # Check if the character is an alphabet letter
        if char.isalpha():
            # If it's a vowel, increment the vowel count
            if char in vowel:
                vowel_count += 1
            # Otherwise, it's a consonant, so increment the consonant count
            else:
                constant_count += 1

    # Print the results
    print(f"vowel_count in given string: {input_string} as {vowel_count}")
    print(f"constant_count in given string: {input_string} as {constant_count}")


# Test the first version with a sample string
input_string = "Shivakiran"
check_count(input_string)


# Version 2: Simplified counting using list comprehensions and sum
def sting_count(text):
    # Define vowels (both uppercase and lowercase)
    vowel = "aeiouAEIOU"

    # Count vowels by checking each character against the vowels set
    vowels_count = sum(1 for char in text if char in vowel)
    # Count consonants by checking alphabet characters not in the vowels set
    constant_count = sum(1 for char in text if char.isalpha() and char not in vowel)

    # Print the results
    print(f"vowel_count in given string: {text} as {vowels_count}")
    print(f"constant_count in given string: {text} as {constant_count}")


# Test the simplified version with the same sample string
text = "Shivakiran"
sting_count(text)
