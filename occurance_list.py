def occurance_list (lst ,  element):
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count

# Example usage
my_list = [1, 2, 3, 4, 2, 3, 2, 5, 2]
element = 2
count = occurance_list(my_list, element)
print(f"The element {element} occurs {count} times in the list.")

def count_all_occurrences (lst):
    occurance = {}

    for item in lst:
        if item in occurance:
            occurance[item] += 1
        else:
            occurance[item] = 1
    return occurance
# Example usage
my_list = [1, 2, 3, 4, 2, 3, 2, 5, 2, 4, 5, 1]
occurrences = count_all_occurrences(my_list)
print("Occurrences of all elements:", occurrences)