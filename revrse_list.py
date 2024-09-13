def reverse_lst (lst):
    reverse_list = []
    for i in range (len(lst)-1,-1,-1):
        reverse_list.append(lst[i])
    return  reverse_list
#----------------------------------------------
#method2 using insert
def revrse_list2(lst):
    rev_list = []
    for i in range(len(lst)):
        rev_list.insert(0, lst[i])
    return  rev_list
#---------calling function-------------------
my_list = [1, 2, 3, 4, 5]
reversed_list = revrse_list2(my_list)

my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_lst(my_list)

print(f"Original List: {my_list}")
print(f"Reversed List: {reversed_list}")

#-------------------------------------------------------------------------


print(f"Original List: {my_list}")
print(f"Reversed List: {reversed_list}")