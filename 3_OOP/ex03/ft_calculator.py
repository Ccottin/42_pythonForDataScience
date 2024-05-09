# map() creates an object that is "lazily evaluated", meaning that its
# computed only on demands. In the exercice, to avoid loosing vectors's
# values, we'll redefine it as a list every time an operation is made

class calculator:
    """a calculator class to do calculation of vector"""

    def __init__(self, object):
        """Initialise the class using a givn vector"""
        self.vector = object

    def __add__(self, object) -> None:
        """Adds the inner vector by object"""
        self.vector = list(map(lambda x: x + object, self.vector))
        print(list(self.vector))

    def __mul__(self, object) -> None:
        """Multiplies the inner vector by object"""
        self.vector = list(map(lambda x: x * object, self.vector))
        print(list(self.vector))

    def __sub__(self, object) -> None:
        """Substracts the inner vector by object"""
        self.vector = list(map(lambda x: x - object, self.vector))
        print(list(self.vector))

    def __truediv__(self, object) -> None:
        """Divides the inner vector by object"""
        if (object == 0):
            return
        self.vector = list(map(lambda x: x / object, self.vector))
        print(list(self.vector))
