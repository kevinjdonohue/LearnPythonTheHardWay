# function that takes two parameters, cheese_count and boxes_of_crackers, and prints out messages with their values
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


# calling the function with integer parameters
print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


# calling the function with integer variables
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# modifying the parameters within the method signature
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# also modifying the parameters within the method signature -- combining defined integer variables and integer parameters
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
