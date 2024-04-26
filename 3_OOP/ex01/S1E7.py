from S1E9 import Character


class Baratheon(Character):
    def __init__(self, first_name: str, is_alive=True,
                 eyes='brown', hairs='dark'):
        """Initialisation of the class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.hairs = hairs
        self.eyes = eyes
        self.familyname = "Baratheon"
    
    def __str__(self):
        """returns a str."""
        return f''

  #  def __repr__(self):
   #     """returns a str."""
    #    return str(self)


class Lannister(Character):
    def __init__(self, first_name: str, is_alive=True,
                 eyes='blue', hairs='light'):
        """Initialisation of the class"""
        self.first_name = first_name
        self.is_alive = is_alive
        self.familyname = "Lannister"
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(self, first_name: str):
        """creates a new Lannister"""
        return Lannister(first_name)

    def __str__(self):
        """returns a str."""
        return str(self)



        
