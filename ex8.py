"""Exercise 8."""

# variable that defines a format string with 4 placeholders
formatter = "{} {} {} {}"

# prints out 1, 2, 3, 4 by passing those values into the format function
print(formatter.format(1, 2, 3, 4))

# prints out strings by passing those values into the format function
print(formatter.format("one", "two", "three", "four"))

# prints out booleans by passing those values into the format function
print(formatter.format(True, False, False, True))

# prints out a total of 16 {}s
# because instead of being treated as a format string
# we're treating the string literally
print(formatter.format(formatter, formatter, formatter, formatter))

# prints out all 4 sentence fragments into a single sentence
# via the formatter's format function
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
