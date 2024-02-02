import sys
from ft_filter import ft_filter


def filterstring(argv: list):
    """This function accepts two arguments: a string(S), and an integer(N). It
    outputs a list of words from S that have a length greater than N."""
    assert (len(argv) == 3) and (isinstance(argv[1], str)) \
        and (argv[2].isdigit()), "the arguments are bad"
    lenght = int(argv[2])
    array = argv[1].split()
    toprint = list(ft_filter(lambda arg: len(arg) > lenght, array))
    print(toprint)


def main():
    try:
        filterstring(sys.argv)
        return (0)
    except AssertionError as e:
        print("Assertion Error: " + e.args[0] if e.args else "")
        return (1)
    except Exception:
        print("Error")
        return (1)


if __name__ == "__main__":
    main()
