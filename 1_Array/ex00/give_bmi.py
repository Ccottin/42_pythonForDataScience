import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    """Take 2 lists of integers or floats in input and returns a list of
        BMI values."""
    try:
        assert isinstance(height, list) and isinstance(weight, list), \
                "Unvalid data type"
        assert (height is not None and weight is not None and
                len(height) == len(weight)), "Unvalid lists size"
        assert all(isinstance(x, float) or isinstance(x, int) for x
                   in weight) and all(isinstance(x, float)
                                      or isinstance(x, int) for x in height), \
            "Lists are not exclusively int or float"
        assert all(x > 0 for x in weight) and all(x > 0 for x in height), \
            "Values cannot be negatives"

        h = np.array(height)
        w = np.array(weight)
        bmi = w / (h ** 2)
        return (list(bmi))

    except AssertionError as e:
        print("Assertion Error: ", str(e))
        return (1)
    except Exception as e:
        print("Error" + e.args[0], str(e))
        return (1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans
    (True if above the limit)."""

    try:  
        assert isinstance(bmi, list) and isinstance(limit, int), \
                "Unvalid data type"
        assert bmi is not None and all(isinstance(x, float) or
               isinstance(x, int) for x in bmi), "List format incorrect"
        assert limit is not None, "Limit format incorrect"
        assert all(x > 0 for x in bmi) and limit > 0, \
            "Values cannot be negatives"
        bmi = np.array(bmi)
        return (list(bmi > limit))

    except AssertionError as e:
        print("Assertion Error: ", str(e))
        return (1)
    except Exception as e:
        print("Error", str(e))
        return (1)
