def longest_word(sentence):
    string = sentence.split()
    longest_word = max(string, key=len)
    return longest_word, len(longest_word)

sentence = "Write a program to find the longest word in a string"
word, length = longest_word(sentence)

print(f"Longest word and length of longest word is: {word}, {length}")
