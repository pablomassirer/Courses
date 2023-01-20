# Program that outputs a string using closure and generator

def string(text):
    value = text

    def iter():
        return (x + "|" for x in text)
    return iter

str1 = string("abcde")
str2 = string("lolpitu")

for s in str2():
    print(s, end="")
