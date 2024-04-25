from numpy import array


def slice_me(family: list, start: int, end: int) -> list:
    """Takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and end
    arguments.
    Numpy provides a slice tool, used as [start:end] to resize an
    array."""
    try:
        assert isinstance(family, list), "provide an array to slice"
        family = array(family)
        print("My shape is :", family.shape)
        family = family[start:end]
        print("My new shape is :", family.shape)
        return (family)

    except AssertionError as e:
        print("AssertionError: ", str(e))
        return (None)
    except Exception as e:
        print("Error: " + str(e))
        return (None)
