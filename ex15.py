"""Exercise 15."""

# from:  as a variant of import, you can use from to specify the module
# and then import to bring in specific names (functions)
# import:  searches for a named module
# and if found binds the results to a name in the local scope
# the sys module we are pulling in the argv function? / library?
from sys import argv

# using argv we are taking in 2 arguments from the terminal,
# the name of our python script and the name of the file we want to open
# pylint: disable=unbalanced-tuple-unpacking
script, filename = argv

# assigning the "file" opened using the open function
# and passing it the name of the file that we took in from the terminal
txt = open(filename)

# printing out a message with the filename that was provided
print(f"Here's your file {filename}:")

# printing out the contents of the file, assigned to the txt variable,
# by calling the read function on the txt (file) without any arguments
print(txt.read())

txt.close()

# printing out a prompt message just before we ask the user for the filename
# print("Type the filename again:")

# assigning user input, captured using the input function
# file_again = input("> ")

# assigning the "file" opened using the open function a
# nd passing it the name of the file we took in from the user via input
# txt_again = open(file_again)

# printing out the contents of the file, assigned to the txt_again variable,
# by calling the read function on the txt_again again without any arguments
# print(txt_again.read())
