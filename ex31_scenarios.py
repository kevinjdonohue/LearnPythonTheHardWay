"""Exercise 31 Scenarios."""


class Scenarios:
    """A scenarios class."""

    good_job = "Good job!"

    def bear_scenario(self):
        """Bear Scenario."""
        print("There's a giant bear here eating a cheese cake.")
        print("What do you do?")
        print("1.  Take the cake.")
        print("2.  Scream at the bear.")

        bear = input("> ")

        bear_eats = "The bear eats your {} off.  " + self.good_job

        if bear == "1":
            print(bear_eats.format("face"))
        elif bear == "2":
            print(bear_eats.format("legs"))
        else:
            print(f"Well, doing {bear} is probably better.")
            print("Bear runs away.")

    def abyss_scenario(self):
        """Abyss Scenario."""
        print("You stare into the endless abyss at Cthulhu's retina.")
        print("1.  Blueberries.")
        print("2.  Yellow jacket clothespins")
        print("3.  Understanding revolvers yelling melodies.")

        insanity = input("> ")

        if insanity in ("1", "2"):
            print("Your body survives powered by a mind of jello.")
            print(f"{self.good_job}")
        else:
            print("The insanity rots your eyes into a pool of muck.")
            print(f"{self.good_job}")

    def alt_scenario(self):
        """Alternative Scenario."""
        print(
            f"You stumble around and fall on a knife and die.\
                  {self.good_job}")
