def are_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        print( f" the give {str1} and {str2} are not anagram")
    elif sorted(str1)==sorted(str2):

        print(f" the give {str1} and {str2} are anagram")
    else:
        print(f" the give {str1} and {str2} are not anagram")

str1 = "EARTH"
str2 = "heart"
are_anagram(str1, str2)

#example2
str1 = "EARTH123"
str2 = "heart"
are_anagram(str1, str2)