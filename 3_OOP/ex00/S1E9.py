from abc import ABC, abstractmethod

#trouver comment gerer les erreurs
#comprendre le decorateur abstract method
#c est deja bien

class Character(ABC):
    """An abstract class to create a character."""
    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        #find a way to assert its a string
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        self.is_alive = False


class Stark(Character):
    """A children class from character"""
