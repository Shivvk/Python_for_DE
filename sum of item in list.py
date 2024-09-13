# Example usage using sum() built-in function
my_list = [1, 2, 3, 4, 5]
total_sum = sum(my_list)
print(f"The sum of all elements in the list is: {total_sum}")

#with sum version2
def sum_of_elements(lst):
    total = 0
    for i in lst:
        total += i
    return total

# Example usage
my_list = [1, 2, 3, 4, 5,10]
total_sum = sum_of_elements(my_list)
print(f"The sum of all elements in the list is: {total_sum}")

