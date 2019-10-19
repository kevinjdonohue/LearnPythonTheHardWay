"""Exercise 4."""

# variable is assigned the integer value 100
cars = 100

# variable is assigned the integer value 4
space_in_a_car = 4

# variable is assigned the integer value 30
drivers = 30

# variable is assigned the integer value 90
passengers = 90

# variable is assigned the result of subtracting drivers from cars which is 70
cars_not_driven = cars - drivers

# variable is assigned the integer value from drivers (30)
cars_driven = drivers

# variable is assigned the result of multiplying cars_driven by space_in_a_car
# which is 120.0
carpool_capacity = cars_driven * space_in_a_car

# variable is assigned the result of drividing passengers (90) by cars_driven
# which is 3.0
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
