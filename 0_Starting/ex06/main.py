import sys
from ft_filter import ft_filter


def main():
    test1 = list("coucou!")
    test2 = {'0': "coucou", "1": "slt", 2: "o"}
    test3 = list()
    test4 = "une chaine de caracreteiu-(u(-_èu-(-4y(-564e"
    test5 = [1,2,3,4,5,6]
    for i in filter(None, test1):
        print(i)
    print("=")
    for i in ft_filter(None, test1):
        print(i)
    print("________")
    for i in (filter(lambda x: x == 'o', test1)):
        print(i)
    print("=")
    for i in (ft_filter(lambda x: x == 'o', test1)):
        print(i)
    print("________")
    for i in filter(lambda x: isinstance(x, str), test1):
        print(i)
    print("=")
    for i in ft_filter(lambda x: isinstance(x, str), test1):
        print(i)
    print("________")
    for i in filter(None, test2):
        print(i)
    print("=")
    for i in ft_filter(None, test2):
        print(i)
    print("________")
    for i in filter(lambda x: isinstance(x, int), test2):
        print(i)
    print("=")
    for i in ft_filter(lambda x: isinstance(x, int), test2):
        print(i)
    print("________")

    for i in filter(None, test3):
        print(i)
    print("=")
    for i in ft_filter(None, test3):
        print(i)
    print("________")
    for i in filter(lambda x: x + 1, test3):
        print(i)
    print("=")
    for i in ft_filter(lambda x: x + 1, test3):
        print(i)
    print("________")
    print(list(filter(lambda x: x.isalpha(), test4)))
    print(list(ft_filter(lambda x: x.isalpha(), test4)))
    print("________")
    print(filter(lambda x: isinstance(x, int), test2))
    print(ft_filter(lambda x: isinstance(x, int), test2))
    print("________")
    for i in filter(lambda x: x % 2 == 0, test5):
        print(i)
    print("=")
    for i in ft_filter(lambda x: x % 2 == 0, test5):
        print(i)


if __name__ == "__main__":
    main()
