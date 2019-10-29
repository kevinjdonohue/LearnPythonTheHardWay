"""Exercise 39."""

states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}

cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

cities["NY"] = "New York"
cities["OR"] = "Portland"

print("-" * 10)

state_formatter = "{} State has: {}"

print(state_formatter.format("NY", cities["NY"]))
print(state_formatter.format("OR", cities["OR"]))

print("-" * 10)

# city_state_formatter = "{}"
