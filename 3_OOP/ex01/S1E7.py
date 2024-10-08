from S1E9 import Character

# The term "<bound method xx.xx [...]>" indicates
# that you're dealing with a method bound to a specific
# instance of the xx class.

# When you use @classmethod, the method receives the class as the first
# argument (cls) instead of an instance (self).
# Best for class-level data or access to the class itself.


class Baratheon(Character):
    """Representing the Baratheon family."""

    def __init__(self, first_name: str, is_alive=True,
                 eyes='brown', hairs='dark'):
        """Initialisation of the class"""

        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Baratheon"
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self) -> str:
        """returns a str by overriding str method.
        f-strings are used to format easily."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """returns a str by overriding str method.
        f-strings are used to format easily."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True,
                 eyes='blue', hairs='light'):
        """Initialisation of the class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True,
                         eyes='blue', hairs='light'):
        """creates a new Lannister."""
        return Lannister(first_name, is_alive, eyes, hairs)

    def __str__(self) -> str:
        """returns a str by overriding str method.
        f-strings are used to format easily."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """returns a str by overriding str method.
        f-strings are used to format easily."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
