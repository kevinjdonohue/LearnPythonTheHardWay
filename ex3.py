"""Exercise 3."""

print("I will now count my chickens:")

# Divides 30 by 6, which is 5, then adds 25 to 5 with a result of 30
print("Hens", 25 + 30 / 6)

# Multiplies 25 by 3, which is 75, then computes 74 modulus 4 which is 3
# and then finally subtracts 3 from 100 to come up with a result of 97
print("Roosters", 100.0 - 25 * 3 % 4)

print("Now I will count the eggs:")

# Adds 3 plus 2 plus 1, which is 6 minus 5, which is 1 plus 4 modulus 2 (0)
# which is 1 minus 1 divided by 4 which is .75 plus 6 which comes to 6.75
print(3.0 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

# Adds 3 plus 2, which is 5 and checks to see if 5 is less than 5 minus 7
# which is negative 2, so the result is False
print(3.0 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2.0)
print("What is 5 - 7?", 5.0 - 7)

print("Oh, that's why it's False")

print("How about some more.")

# 5 is greater than -2 which is True
print("Is it greater?", -2.0 < 5)

# 5 is greater than or equal to -2 which is True
print("Is it greater or equal?", -2 <= 5.0)

# 5 is less than or equal to -2 which is False
print("Is it less or equalr?", -2.0 >= 5)
