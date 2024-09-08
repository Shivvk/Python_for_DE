def find_length (string):
    count = 0
    for char in string:
        count +=1
    return count
# Example usage
string = "Hello, world!"
length = find_length(string)
print(f"The length of the string '{string}' is: {length}")

#-------------------------------------- version2
string = "Hello, world!"
print (f"the length of string : ", sum([1 for i in string]))

#-------------------------------- Other question count the no of words without length
string = "Hello, world!"
string2 = string.split(" ")
count2 = 0
for char in string2:
    count2 +=1
print (f"the no of words in  string : ", count2)
