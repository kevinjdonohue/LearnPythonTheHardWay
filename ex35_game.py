"""Exercise Game Class."""

from ex35_rooms import Rooms


class Game(object):
    """Game."""

    def __init__(self):
        """Game Constructor."""
        self.r = Rooms()

    def start(self):
        """Start."""
        print("You are in a dark room.")
        print("THere is a door to your right and left.")
        print("Which one do you take?")

        choice = input("> ")

        if choice == "left":
            self.r.bear_room()
        elif choice == "right":
            if not self.r.cthulhu_room():
                self.start()
        else:
            self.r.dead("You stumble around the room until you starve.")
