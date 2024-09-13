# Function to remove duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

# Example usage
my_list = [1, 2, 6, 7, 2, 3, 4, 4, 5]
print("Original List:", my_list)
unique_list = remove_duplicates(my_list)
print("List after removing duplicates:", unique_list)
#---------------------------------------------
def remove_duplicates_preserve_order(lst):
    present = set()
    new_lst = []
    for i in lst:
        if i not in present:
            new_lst.append(i)
            present.add(i)
    return new_lst

# Example usage
my_list = [1, 2, 2, 3,7,7, 4, 4, 5]
print("Original List:", my_list)
unique_list = remove_duplicates_preserve_order(my_list)
print("List after removing duplicates (order preserved):", unique_list)

