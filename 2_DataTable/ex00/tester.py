from load_csv import load


def main():
    print(load("life_expectancy_years.csv"))
    print(load(""))
    print(load("coucou"))
    print(load(123))
    print(load("__pycache__"))


if __name__ == '__main__':
    main()
