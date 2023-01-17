
"""Method to list BaseException subclasses in alphabetical order """

def print_exception_tree(thisclass, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(thisclass.__name__)
    subclasses = [subclass.__name__ for subclass in thisclass.__subclasses__()]
    subclasses.sort()

    for str_subclasses in subclasses:
        for subclass in thisclass.__subclasses__():
            if subclass.__name__ == str_subclasses:
                print_exception_tree(subclass, nest + 1)


print_exception_tree(BaseException)
