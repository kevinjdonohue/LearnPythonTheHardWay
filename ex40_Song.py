from abc import ABCMeta, abstractmethod


class Song(metaclass=ABCMeta):
    @abstractmethod
    def sing_me_a_song(self):
        pass

    @abstractmethod
    def sing_to_me(self, lyrics: list):
        pass
