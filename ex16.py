"""Exercise 16."""

# import from the sys module the argv function
from sys import argv

# from the terminal, capture two values, the script name and the filename
# that you want users to manipulate
# pylint: disable=unbalanced-tuple-unpacking
script, filename = argv

# printing out the filename entered as well as instructions on
# how to "use" the application -- either hitting Ctrl+C or Return
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print(f"If you do want that, hit RETURN.")

# requesting input with a ? as the cursor
input("?")

# printing out an informational message right before opening the file
# via its filename, provided by the user
print("Opening the file...")

# open the file via the filename passed in, but this time we pass the 'w' mode
# which indicates that we want to open the file for writing
target = open(filename, 'w')

# print('Truncating the file.  Goodbye!')
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

formatter = "{}\n {}\n {}\n"

file_contents = formatter.format(line1, line2, line3)

target.write(file_contents)
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()
