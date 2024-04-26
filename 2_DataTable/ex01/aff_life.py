import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program will look for France's data into life_expetancy
    csv, then display a graph representing it using matplotlib.
    DataFrame.T is to transpose columns to rows and vice-versa.
    DataFrame.plot() uses plt.plot() function."""
    try:
        data = load("life_expectancy_years.csv")
        assert data is not None, "No data provided"
        france_data = data[data['country'] == 'France'].set_index('country')
        france_data = france_data.T

        print(france_data)
        plt.plot(france_data)
        plt.title('France Life expectancy Projections')
        plt.ylabel('life expectancy')
        plt.xlabel('year')
        plt.xticks(range(0, 2100 - 1800, 40))
        plt.show()
        plt.close()

    except AssertionError as e:
        print("Assertion Error: ", str(e))
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
