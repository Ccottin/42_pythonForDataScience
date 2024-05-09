from S1E7 import Baratheon, Lannister

# Les trois regles de la c3 linearization
# Priorité aux classes parentes :
# 1/ Python commence par chercher dans les classes parentes avant
# de chercher dans les classes enfants.
# 2/ Ordre de recherche cohérent : L'ordre dans lequel Python cherche
# les méthodes est cohérent : Si une classe apparaît avant une autre
# dans l'ordre de recherche des méthodes d'une classe, elle doit aussi
# apparaître avant dans l'ordre de recherche des méthodes de toutes
# ses sous-classes.
# 3/ Priorité aux classes enfants :
# Si une classe enfant et une classe parente ont une méthode avec
# le même nom, Python choisira la méthode de la classe enfant.
# Un algo va creer un MRO (Method-Resolution Order) base sur ces trois
# regles, et Python creera la classe en donnant priorite au methodes les
# plus a gauche du MRO


class King(Baratheon, Lannister):
    """Creates a king."""

    def set_eyes(self, eyes: str):
        """change eye color"""
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        """change hair color"""
        self.hairs = hairs

    def get_eyes(self):
        """get eyes color"""
        return (self.eyes)

    def get_hairs(self):
        """get hairs color"""
        return (self.hairs)
