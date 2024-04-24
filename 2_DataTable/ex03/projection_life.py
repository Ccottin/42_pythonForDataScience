from load_csv import load
import matplotlib.pyplot as plt
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
        display = pd.concat([ley, gdp])

        print(ley, gdp)

    except Exception as e:
        print("Error:", str(e))


if __name__ == "__main__":
    main()
