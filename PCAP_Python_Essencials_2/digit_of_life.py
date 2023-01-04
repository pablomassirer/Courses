b_day = input("")
digits = [int(num) for num in b_day]
digits_of_life = sum(digits)

while len(str(digits_of_life)) > 1:
    digits_of_life = [int(num) for num in str(digits_of_life)]
    digits_of_life = sum(digits_of_life)
print(digits_of_life)

# Sample input: 19991229 | output: 6
# Sample input: 20000101 | output: 4
