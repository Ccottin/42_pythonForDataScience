import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program will look for France's data into life_expetancy
    csv, then display a graph representing it using matplotlib."""
    try:
        data = load("life_expectancy_years.csv")
        assert data is not None, "No data provided"
        life_data = data[data['France']] #itsabolutely not this
        print(life_data)
        time = data['country']
        plt.plot(time, life_data)
        plt.ylabel = 'life expectancy'
        plt.xlabel = 'year'
        plt.title = 'France Life expectancy Projections'
        plt.show()
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
