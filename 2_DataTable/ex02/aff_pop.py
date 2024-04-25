import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program will display population total and projection
    for France and Mali."""

    try:
        data = load("population_total.csv")
        assert data is not None, "No data provided"

        countries = ['France', 'Mali']
        data = data[data.country.isin(countries)]
        data = data.iloc[:, :data.columns.get_loc('2051')]
        data = data.set_index('country') 

        print(data)
        data = data.replace('k', '000')
        data = data.map(lambda x: float(x.replace('M', '')) * 1e6
                        if 'M' in x else float(x))

        print(data)

        data = data.T

        data.plot(kind='line',
                 title='France Life expectancy Projections',
                 ylabel='population', xlabel='year')
        plt.show()
        plt.close()

    except Exception as e:
        print("Error:", str(e))
    except AssertionError as e:
        print("Assertion Error: ", str(e))


if __name__ == "__main__":
    main()
