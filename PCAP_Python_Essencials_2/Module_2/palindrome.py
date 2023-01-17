string = input("")
string = string.replace(" ", "").lower()
if string[::-1] == string:
    print("It's a palindrome.")
else:
    print("It's not a palindrome")

# Sample input: Ten animals I slam in a net | output: It's a palindrome
# Sample input: Eleven animals I slam in a net | output: It's not a palindrome
