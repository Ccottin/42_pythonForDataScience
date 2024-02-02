
class iterator:

    def __init__(self, c_list):
        self.list = c_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.list):
            raise StopIteration
        return self.list[self.index - 1]


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true.
    This is ft_filter; a home-made version"""

    if (function is None):
        return (iterator([elem for elem in iterable if elem]))
    else:
        return (iterator([elem for elem in iterable if function(elem)]))
