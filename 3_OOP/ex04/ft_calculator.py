# Decorators are used to modify the behavior of a function without
# changing it. Syntax can be 'def decorator(ft) :' then, later on,
# you can apply it to a function by adding '@decorator' above it

# The @staticmethod decorator is used to define static methods within a
# class. Static methods are the methods that can be called without creating
# an instance of the class. Static methods are often used when they don't
# have to access object-related parameters and are more related to the
# class as a whole.

# The dot product is a special way to combine two vectors into a single number,
# which tells us how much they work together in the same direction.
# 0 means they are perpendicular
# Positives numbers -> they go the same way, the greater, the more
# Negatives numbers -> they go in opposite directions, the smaller, the more

class calculator:
    """Class calculating two vectors together"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Do a dot product of two vectors"""
        dotProduct = 0
        for i in V1:
            dotProduct += i * V2[V1.index(i)]
        print("Dot product is:", dotProduct)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Will add two vectors"""
        res = [0] * len(V1)
        for i in V1:
            res[V1.index(i)] = i + V2[V1.index(i)]
        print("Add Vector is :", ([float(f'{disp:.1f}') for disp in res]))

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Will substract two vectors"""
        res = [0.0] * len(V1)
        for i in V1:
            res[V1.index(i)] = i - V2[V1.index(i)]
        print("Sous Vector is :", ([float(f'{disp:.1f}') for disp in res]))
