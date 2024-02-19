import sys

size = len(sys.argv)
sys.tracebacklimit = 0
assert size < 3, "more than one argument is provided\n"
assert size > 1, "no argument is provided\n"
if (size == 2) :
    if (sys.argv[1][0] == '-') :
        sys.argv[1] = sys.argv[1][1:]
    assert sys.argv[1].isdecimal(), "argument is not an integer\n"
    if (int(sys.argv[1]) % 2 == 0) :
        print("I'm Even.")
    else :
        print("I'm Odd.")

print ("")
