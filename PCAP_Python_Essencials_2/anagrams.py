word_1 = input("").replace(" ", "").lower()
word_2 = input("").replace(" ",  "").lower()
count = 0

for letter in word_1:
    if letter in word_2:
        count += 1
if count == len(word_2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Sample input: Listen; input2: Silent | output: Anagrams
# Sample input: modern; input2: norman | output: Not anagrams
