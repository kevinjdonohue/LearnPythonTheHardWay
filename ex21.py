"""Exercise 21.

simple calculator functions
"""


def add(a, b):
    """Add."""
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    """Subtract."""
    print(f"SUBTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    """Multiply."""
    print(f"MULTIPYING {a} * {b}")
    return a * b


def divide(a, b):
    """Divide."""
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(4421, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"That becomes: {what}  Can you do it by hand?")
