import matplotlib.pyplot as plt
from load_csv import load


def ft_convert(x):
    conv_dict = {"K": 10 ** 3,
                 "M": 10 ** 6,
                 "B": 10 ** 9}
    for i in conv_dict:
        if i in x:
            x = str(x)
            x = float(x.upper().replace(i, '')) * float(conv_dict[i])
            return (x)
    return (float(x))


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

        data = data.T
        data = data.map(lambda x: ft_convert(x))

        plt.plot(data)
        plt.legend(['Mali', 'France'], loc=4)
        plt.title('Population Projection')
        plt.ylabel('Population')
        plt.xlabel('Year')
        plt.xticks(range(0, 2050 - 1800, 40))
        plt.yticks(range(0, (80 * 10 ** 6), (20 * 10 ** 6)),
                   ['', '20M', '40M', '60M'])
        plt.ylim(bottom=1)

        plt.show()
        plt.close()

    except Exception as e:
        print("Error:", str(e))
    except AssertionError as e:
        print("Assertion Error: ", str(e))


if __name__ == "__main__":
    main()
