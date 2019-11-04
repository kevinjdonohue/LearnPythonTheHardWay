"""Exercise 35 Rooms."""

from sys import exit


class Rooms(object):
    """Rooms Class."""

    def gold_room(self):
        """Gold Room."""
        print("This room is full of gold.  How much do you take?")

        choice = input("> ")

        if "0" in choice or "1" in choice:
            how_much = int(choice)
        else:
            self.dead("Man, learn to type a number.")

        if how_much < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
        else:
            self.dead("You greedy bastard!")

    def bear_room(self):
        """Bear Room."""
        print("There is a bear here.")
        print("The bear has a bunch of honey.")
        print("The fat bear is in front of another door.")
        print("How are you going to move the bear?")

        bear_moved = False

        while True:
            choice = input("> ")

            if choice == "take honey":
                self.dead("The bear looks at you then slaps your face off.")
            elif choice == "taunt bear" and not bear_moved:
                print("The has moved from the door.")
                print("You can go through it now.")
                bear_moved = True
            elif choice == "taunt bear" and bear_moved:
                self.dead("The bear gets pissed off and chews your leg off.")
            elif choice == "open door" and bear_moved:
                self.gold_room()
            else:
                print("I got no idea what that means.")

    def cthulhu_room(self):
        """Cthulhu Room."""
        print("Here you see the great evil Cthulhu.")
        print("He, it, whatever stares at you and you go insane.")
        print("Do you flee for your life or eat your head?")

        choice = input("> ")

        print(choice)

        if "flee" in choice:
            self.start()
        elif "head" in choice:
            self.dead("Well that was tasty!")
        else:
            self.cthulhu_room()

    def dead(self, why):
        """Dead."""
        print(why, "Good job!")
        exit(0)
