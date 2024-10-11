# if you want to access a variable from within a nested
# function; you can use nonlocal (see l.32)

# Nested or Inner function are used to protect ect.
# and mostly are a base to decorators

def square(x: int | float) -> int | float:
    """returns the square of provided argument"""
    try:
        return x ** 2
    except Exception as e:
        print("Error: ", e.str())
        return (None)


def pow(x: int | float) -> int | float:
    """returns the power of provided argument argument"""
    try:
        return x ** x
    except Exception as e:
        print("Error: ", e.str())
        return (None)


def outer(x: int | float, function) -> object:
    """returns an object which applies provided function to x according to how
    many time the object is called"""
    try:
        count = 0

        def inner() -> float:
            nonlocal count
            temp = x
            i = 0

            while i < count:
                i = i + 1
                temp = function(temp)
            count = count + 1
            return function(temp)

        return (inner)

    except Exception as e:
        print("Error: ", e.str())
        return (None)
