from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.axis as axis
import matplotlib.ticker as ticker
import pandas as pd

def main():
    '''Displays the projection of life expectancy in relation to the gross
        national product of the year 1900 for each country.'''
    try:
        ley = load("life_expectancy_years.csv")
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        assert ley is not None and gdp is not None, "Not enought data provided"

        ley = ley['1900']
        gdp = gdp['1900']
        
        plt.semilogx(gdp, ley, "ob")
        plt.title('1900')
        plt.ylabel('Life Expectancy')
        plt.xlabel('Gross domestic product')

# finir ca demain
        axis.Axis.set_major_locator(ticker.FixedLocator([0, 10]))
      #  axis.Axis.set_ticklabels(['300', '1k', '10k'])
        plt.show()
        plt.close()

    except AssertionError as e:
        print("Assertion Error: ", str(e))
    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
