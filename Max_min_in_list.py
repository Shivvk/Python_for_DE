# Function to find the maximum and minimum elements in a list
def find_max_min(lst):
    if len(lst) == 0:
        return None, None  # If the list is empty, return None

    max_element = lst[0]
    min_element = lst[0]

    for num in lst:
        if num > max_element:
            max_element = num
        if num < min_element:
            min_element = num

    return max_element, min_element


# Example usage
my_list = [15, 22, 84, 14, 56, 3, 78, 100]
max_value, min_value = find_max_min(my_list)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")
