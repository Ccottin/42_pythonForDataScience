import sys


def morse_encoding(message: str):
    """This function will encode in Morse any given string. It also
    detects non alphnumerics characters. In case of multiple space characters,
    they all merge into one."""
    morse_dict = {
            "A": "._",   "B": "_...", "C": "_._.", "D": "_..",
            "E": ".",    "F": ".._.", "G": "__.",  "H": "....",
            "I": "..",   "J": ".___", "K": "_._",  "L": "._..",
            "M": "__",   "N": "_.",   "O": "___",  "P": ".__.",
            "Q": "__._", "R": "._.",  "S": "...",  "T": "_",
            "U": ".._",  "V": "..._", "W": ".__",  "X": "_.._",
            "Y": "_.__", "Z": "__..",
            "0": "_____", "1": ".____", "2": "..___",
            "3": "...__", "4": "...._", "5": ".....",
            "6": "_....", "7": "__...", "8": "___..",
            "9": "____.",
            " ": "/", "\n": "/", "\t": "/", "\r": "/", "\b": "/",
            "\f": "/", "\v": "/"
            }

    encoded = ""
    message = message.upper()
    for x in message:
        if (encoded == ""):
            encoded = encoded + morse_dict[x]
        else:
            encoded = encoded + " " + morse_dict[x]
    print(encoded)


def main():
    """Args are checked in main thanks to an 'all' function.
    The all() function returns True if all items in an iterable are true,
    otherwise it returns False."""
    try:
        assert (len(sys.argv) == 2 and isinstance(sys.argv[1], str)
                and all(x.isalnum() or x.isspace() for x in sys.argv[1])
                ), "the arguments are bad"
        morse_encoding(sys.argv[1])
    except AssertionError as e:
        print("Assertion Error:", e.args[0] if e.args else "")
        return (1)
    except Exception as e:
        print("Error", e.args[0] if e.args else "")
        return (1)


if __name__ == "__main__":
    main()
