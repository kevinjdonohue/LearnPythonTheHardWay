"""Exercise 5."""


def convert_inches_to_centimeters(inches):
    """Convert Inches to Centimeters."""
    return inches * 2.54


def convert_pounds_to_kilograms(pounds):
    """Convert Pounds to Kilograms."""
    return pounds / 2.2046


name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
height_in_centimeters = convert_inches_to_centimeters(height)
weight = 180  # lbs
weight_in_kilograms = convert_pounds_to_kilograms(weight)
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"Which is {height_in_centimeters} centimeters tall.")
print(f"He's {weight} pounds heavy.")
print(f"He's {weight_in_kilograms} kilos heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
