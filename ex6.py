"""Exercise 6."""

# variable assigned the integer value 10
types_of_people = 10

# variable assigned a format string that contains the types_of_people variable
x = f"There are {types_of_people} types of people."

# variable assigned the string "binary"
binary = "binary"

# variable assigned the string don't
do_not = "don't"

# variable assigned a format string that contains the binary
# and do_not variables
y = f"Those who know {binary} and those who {do_not}."

# printing out x
print(x)

# printing out y
print(y)

# printing out a formatted string with x in it
print(f"I said: {x}")

# printing out a formatted string with y in it
print(f"I also said: '{y}'")

# assigning the value False to a variable
hilarious = False

# variable assigned a string with a format placeholder in it
joke_evaluation = "Isn't that joke so funny?! {}"

# printing out the formatted string
# inside, calling the format function on the joke_evaluation string
# in order to insert the hilarious variable into itself
print(joke_evaluation.format(hilarious))

# variable assigned a string
w = "This is the left side of..."

# variable assigned another string
e = "a string with a right side."

# printing out both previously defined strings by concatenating them together
# via the plus (+) operator inside the print statement
print(w + e)
