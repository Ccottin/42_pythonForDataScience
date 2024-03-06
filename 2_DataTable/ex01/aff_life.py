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
        france_data.plot(kind='line',
                         title='France Life expectancy Projections',
                         ylabel='life expectancy', xlabel='year', legend=False)
        plt.show()
        plt.close()

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
