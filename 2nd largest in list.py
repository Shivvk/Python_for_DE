def second_largest (lst):
    if len(lst)<2:
        return "List must contain at least two elements."

    largest = second_largest = lst[0]

    for item in lst:
        if item > largest:
            second_largest = largest
            largest = item
        elif   second_largest < item < largest:
            second_largest = item

    return  second_largest

# Example usage
my_list = [12, 35, 1, 10, 34, 1]
result = second_largest(my_list)
print(f"The second largest number in the list is: {result}")