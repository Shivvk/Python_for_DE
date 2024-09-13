# Function to perform bubble sort on a list of numbers
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]
print(my_list)
sort_list =  bubble_sort(my_list)  # Sorts the list in place
print(f"Sorted List: {sort_list}")
