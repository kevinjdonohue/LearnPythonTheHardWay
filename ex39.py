"""Exercise 39."""

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {"CA": "San Francisco", "MI": "Detroit", "FL": "Jacksonville", "NY": "New York", "OR": "Portland"}

print("-" * 10)

cities_formatter = "{} State has: {}"

print(cities_formatter.format("NY", cities["NY"]))
print(cities_formatter.format("OR", cities["OR"]))

print("-" * 10)

states_formatter = "{}'s abbreviation is: {}"

# print some states
print(states_formatter.format("Michigan", states["Michigan"]))
print(states_formatter.format("Florida", states["Florida"]))

print("-" * 10)

cities_states_formatter = "{} has: {}"

# do it by using the state then cities dict
print(cities_states_formatter.format("Michigan", cities[states["Michigan"]]))
print(cities_states_formatter.format("Florida", cities[states["Florida"]]))

print("-" * 10)

# print every state abbreviation
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print("-" * 10)

# print every city in state
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print("-" * 10)

# now do both at the same time
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print("-" * 10)

if not state:
    print("Sorry, not Texas.")

# get a city with a default value
city = cities.get("TX", "Does Not Exist")
print(f"The city for the state 'TX' is: {city}")
