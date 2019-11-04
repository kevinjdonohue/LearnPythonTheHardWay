"""Exercise 40."""
from ex40_MySong import MySong, FakeSong

happy_birthday_lyrics = ["Happy Birthday to you", "I don't want to get sued", "So I'll stop right there."]

happy_birthday = MySong(happy_birthday_lyrics)

bulls_on_parade_lyrics = ["They rally around the family", "With pockets full of shells"]

bulls_on_parade = MySong(bulls_on_parade_lyrics)

happy_birthday.sing_me_a_song()
happy_birthday.sing_to_me(["These are some fake happy birthday lyrics!"])

bulls_on_parade.sing_me_a_song()
bulls_on_parade.sing_to_me(["These are some fake bulls on parade lyrics!"])

l = bulls_on_parade.return_lyrics([1, 2, 3, 4])

print(l)
