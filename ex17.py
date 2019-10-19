"""Exercise 17."""

from sys import argv
# from os.path import exists

# script, from_file, to_file = argv

# print(f"Copying from {argv[1]} to {argv[2]}")

# in_file = open(argv[1])
# indata = in_file.read()

with open(argv[1]) as in_file:
    with open(argv[2], 'w') as out_file:
        out_file.write(in_file.read())

# print(f"The input file is {len(indata)} bytes long")

# print(f"Does the output file exist?  {exists(to_file)}")
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(argv[2], 'w')
# out_file.write(indata)

# print(f"Alright, all done.")

# out_file.close()
# in_file.close()
