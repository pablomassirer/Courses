""" Just Work with Spaces """
def mysplit(strng):
    splited_list = []
    word = ""
    n_spaces = strng.count(" ")
    c_space = 0
    len_str = len(strng.strip())
    c_len_str = 0
    for letter in strng.strip():
        if letter != " ":
            word += letter
        if c_len_str == len_str - 1 and word != "":
            splited_list.append(word)
        if letter == " " and word != "":
            splited_list.append(word)
            c_space += 1
            word = ""
        c_len_str += 1
    return splited_list

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
