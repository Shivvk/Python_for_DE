#check the number of words
def no_of_words (string):
    words = string.split(" ")
    words_count = len(words)
    return words_count

string = "Python is easy to learn"
print(f"the total number of words in given string : {string} : ",no_of_words (string))

#check whether given string is digit

def is_digit(input_string):
    return input_string.isdigit()

input_string = "1234"
print (f"the given string {input_string} is digit :", is_digit(input_string))

input_string2 = "12asas34"
print (f"the given string {input_string2} is digit :", is_digit(input_string2))