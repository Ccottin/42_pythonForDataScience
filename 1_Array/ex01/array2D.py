from numpy import array


def slice_me(family: list, start: int, end: int) -> list:
    """Numpy provides a slice tool, used as [start:end] to resize an
    array."""
    try:
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
