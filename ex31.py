"""Exercise 31."""

from ex31_scenarios import Scenarios

print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?""")

door = input("> ")

s = Scenarios()

if door == "1":
    s.bear_scenario()

elif door == "2":
    s.abyss_scenario()

else:
    s.alt_scenario()
