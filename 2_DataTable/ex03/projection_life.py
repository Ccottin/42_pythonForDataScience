from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Displays the projection of life expectancy in relation to the gross
        national product of the year 1900 for each country."""
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
        plt.xticks([300, 1000, 10000], labels=['300', '1k', '10k'])

        plt.show()
        plt.close()

    except AssertionError as e:
        print("Assertion Error: ", str(e))
    except Exception as e:
        print("Error:", str(e))


#pense a remodifier ton code en fonction
    def ft_retry(lst):
    for x in lst:
        x = str(x)
        if 'K' in x.upper():
            x = float(x.upper().replace('K', '')) * 1e3
        elif 'M' in x.upper():
            x = float(x.upper().replace('M', '')) * 1e6
        else:
            x = float(x)
    return (lst)

if __name__ == "__main__":
    main()
