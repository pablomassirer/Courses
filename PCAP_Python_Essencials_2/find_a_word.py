"""Program to know if the letters of a giving word is presented in a string"""

word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

index = 0
splited_word = [letter for letter in word] # split the word to search
dict_letter_index = {}
for letter_find in splited_word:
    if letter_find in strn: # Verifies if letter is in the string
        index = strn.find(letter_find, index) # captures the index of the letter
        if index != -1:
            dict_letter_index[letter_find] = index #if the letter is found add it alongside its index

# Compares if the original collection of letters is equal to the sorted version
# to finally find if their index order match with the sorted one.
# In that way we know the sequence of occurences of the letters in the string is valid and present.
if list(dict_letter_index.values()) == sorted(dict_letter_index.values()):
    print("Yes")
else:
    print("No")


# Sample input: donor; inpout2: Nabucodonosor | output: Yes
# Sample input: donut; input2: Nabucodonosor | output: No
