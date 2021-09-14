# To find file path on linux:  readlink -f [file].py
def create_file():
    with open('/home/pablomassirer/DevStuff/DevCourses/Udacity_AI_programming_with_Python/Scripting/Files/file2.txt', 'w') as f:
        writing_file = f.write('Hey there! Again.')

def show_file():
    for i in range(1,3):
        with open('/home/pablomassirer/DevStuff/DevCourses/Udacity_AI_programming_with_Python/Scripting/Files/file{}.txt'.format(i)) as f:
            show_content = f.read()
            print(show_content)

show_file()
