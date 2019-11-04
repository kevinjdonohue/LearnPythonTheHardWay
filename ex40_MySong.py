"""MySong."""
from ex40_Song import Song
from typing import List


class MySong(Song):

    def __init__(self, lyrics: List[str]):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def sing_to_me(self, lyrics: List[str]):
        for line in lyrics:
            print(line)

    def return_lyrics(self, lyrics: List[str]) -> List[str]:
        return lyrics


class FakeSong(Song):

    def __init__(self, lyrics: list):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        print('fake song lyrics')

    def sing_to_me(self, lyrics: list):
        print(f"fake song lyrics: {lyrics}")