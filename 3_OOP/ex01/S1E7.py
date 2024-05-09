from S1E9 import Character

# The term "<bound method xx.xx [...]>" indicates
# that you're dealing with a method bound to a specific
# instance of the xx class


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

    def __str__(self):
        """returns a str."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """returns a str."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """Representing the Lannister family."""

    def __init__(self, first_name: str, is_alive=True,
                 eyes='blue', hairs='light'):
        """Initialisation of the class"""
        print("test =", first_name)
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(first_name: str, is_alive: bool):
        """creates a new Lannister"""
        return Lannister(first_name)

    def __str__(self):
        """returns a str."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """returns a str."""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
