string = input("Value to be shifted: ")
shift_value = int(input("Shift value: "))
cipher = ""

for letter in string:
    l_num = ord(letter)
    if letter.isalpha():
        l_num += shift_value
        if l_num > ord("z") and letter.islower():
            shift_value_2 = shift_value - (ord("z") - ord(letter)) - 1
            l_num = ord("a") if shift_value_2 == 0 else ord("a") + shift_value_2
        elif l_num > ord("Z") and letter.isupper():
            shift_value_2 = shift_value - (ord("Z") - ord(letter)) - 1
            l_num = ord("A") if shift_value_2 == 1 else ord("A") + shift_value_2
    cipher += chr(l_num)
print(cipher)

"""Test Data"""

# Sample input: abcxyzABCxyz 123; input2: 2 | output: cdezabCDEzab 123
# Sample input: The die is cast; input2: 25 | output: Sgd chd hr bzrs
