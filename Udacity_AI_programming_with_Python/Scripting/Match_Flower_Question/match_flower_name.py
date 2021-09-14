# Write your code here

# HINT: create a dictionary from flowers.txt
def create_flower_dict(filename):
    flowers_list = []
    flowers_dict = {}
    with open(filename, 'r') as f:
        flowers_list = [flower.split(': ') for flower in f]
    for flower in flowers_list:
        flowers_dict[flower[0]] = flower[1].strip()
    return flowers_dict
# HINT: create a function to ask for user's first and last name
def user_flower_name():
    flowers_dict = create_flower_dict("flowers.txt")
    name = input('What\'s your name? > ')
    if name[0].upper() in flowers_dict.keys():
      flower = flowers_dict.get(name[0].upper())
# print the desired output
    print(f"Unique flower name with the first letter of your name: {flower}.")

user_flower_name()
