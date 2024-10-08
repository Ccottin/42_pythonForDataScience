from abc import ABC, abstractmethod


class Character(ABC):
    """An abstract class to create a character. 'pass' keyword
        is used to define init method in every children class."""
    @abstractmethod
    def __init__(self, first_name: str, is_alive=True):
        """Initialisation of the class"""
        pass

    def die(self):
        """Die method turning is alive from true to false"""
        self.is_alive = False


class Stark(Character):
    """A children class from character"""

    def __init__(self, first_name: str, is_alive=True):
        """Initialisation of the class"""
        self.first_name = first_name
        self.is_alive = is_alive
