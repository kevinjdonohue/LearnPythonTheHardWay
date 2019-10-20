"""Exercise 33."""


numbers = []


def print_numbers(upper_bound, increment_by):
    """Print Numbers."""
    i = 0
    while i < upper_bound:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += increment_by
        print(f"Numbers now:  {numbers}")
        print(f"At the bottom i is {i}")


print_numbers(10, 2)

print("The numbers: ")

for num in numbers:
    print(num)
