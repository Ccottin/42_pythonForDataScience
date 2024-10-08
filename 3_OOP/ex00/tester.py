from S1E9 import Stark


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    print("---")
    test = Stark("./__pycache__")
    print(test.__dict__)
    test = Stark("")
    print(test.__dict__)
    test = Stark(None)
    print(test.__dict__)
    test = Stark(123)
    print(test.__dict__)
    try:
        test = Stark()
        print(test.__dict__)
    except Exception as e:
        print("Error :", e)
    # hodor = Character("hodor")


if __name__ == "__main__":
    main()
