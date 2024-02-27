import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    try:
        family = np.array(family)
        print("My shape is :", family.shape)
        
    except AssertionError as e:
        print("AssertionError: " + e.args[0] if e.args else '')
        return (None)
    except Exception as e:
        print("Error: " + e.args[0] if e.args else '')
        return (None)
