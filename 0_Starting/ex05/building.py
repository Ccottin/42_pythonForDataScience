import sys


def building(line: str):
    """This function will count every char and make a total of uppercase,
    lowercase, punctuation marks, spaces and digits.
    Punctuation marks are the one defined in library string, as
    'string.punctuation' shall output."""

    if (line is None or line == ''):
        return (1)
    digits = 0
    lowercases = 0
    uppercases = 0
    punctuations = 0
    whitespaces = 0
    punct_str = "!\"#$%&'()*+, -./:;<=>?@[\\]^_`{|}~"

    for i in line:
        if (i.isdigit()):
            digits += 1
        elif (i.islower()):
            lowercases += 1
        elif (i.isupper()):
            uppercases += 1
        elif (i.isspace()):
            whitespaces += 1
        elif (punct_str.find(i)):
            punctuations += 1
        else:
            assert True, (i + ": unpredicted character detected")

    print("The text contains", len(line), "characters:\n", uppercases,
          "upper letters\n", lowercases,  "lower letters\n", punctuations,
          "punctuation marks\n", whitespaces, "spaces\n", digits, "digits")
    return (0)


def main():
    """The main function is used to check potentials issues, then launch
        appropriate function"""

    line: str = ''
    mark = 1

    try:
        while (mark):
            assert len(sys.argv) < 3, "too many arguments"
            if (len(sys.argv) < 2 or sys.argv[1] is None):
                print("What is the text to count?")
                for line in sys.stdin:
                    break
            else:
                line = sys.argv[1]
            mark = building(line)
        return (0)

    except AssertionError as e:
        print("Assertion Error: " + e.args[0] if e.args else "")
        return (1)

    except Exception:
        print("Error")
        return (1)


if __name__ == "__main__":
    main()
