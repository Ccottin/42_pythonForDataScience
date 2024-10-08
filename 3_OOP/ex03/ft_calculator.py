# map() returns an iterator.
# It creates an object that is "lazily evaluated", meaning that its
# computed only on demands. In the exercice, to avoid loosing vectors's
# values, we'll redefine it as a list every time an operation is made.
# By forcing its immediate evaluation (wrapping into list), we get the
# actual values stored as a list

# calculation of vector with a scalar (a constant) = the operations apply
# to each component of the vector individually.

class calculator:
    """a calculator class to do calculation of vector"""

    def __init__(self, object):
        """Initialise the class using a givn vector"""
        self.vector = object

    def __add__(self, object) -> None:
        """Adds the inner vector by object"""
        self.vector = list(map(lambda x: x + object, self.vector))
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplies the inner vector by object"""
        self.vector = list(map(lambda x: x * object, self.vector))
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substracts the inner vector by object"""
        self.vector = list(map(lambda x: x - object, self.vector))
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divides the inner vector by object"""
        if (object == 0):
            print("Error")
            return
        self.vector = list(map(lambda x: x / object, self.vector))
        print(self.vector)
