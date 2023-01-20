def read_int(prompt, min, max):
    while True:
        try:
            number = int(input(prompt))
            assert min < number < max
            return number
        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")
        except:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    