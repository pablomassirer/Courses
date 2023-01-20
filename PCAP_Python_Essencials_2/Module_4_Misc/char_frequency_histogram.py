from os import strerror

# Program to validate n ocurrences of same letter in given data
try:
    text = input("Enter the name of the file to analyze: ").lower()

    file = open("test.txt", "wt")
    file.write(text)

    file = open("test.txt", "rt")
    content = file.read()
    dic_count = {}

    for letter in content:
        dic_count[letter] = 1 if letter not in dic_count \
                                else dic_count.get(letter) + 1

    dic_count = dict(sorted(dic_count.items(), key=lambda x: x[0]))
    dic_count = dict(sorted(dic_count.items(), key=lambda x: x[1], reverse=True))
    output = list(map(lambda x, y: str(x) + " --> " + str(y) \
                                        ,dic_count.keys() \
                                        ,dic_count.values()))

    output = "\n".join(output)
    print(f"\n{output}")
except IOError as e:
    print("I/O error occurred: ", strerror(e))
