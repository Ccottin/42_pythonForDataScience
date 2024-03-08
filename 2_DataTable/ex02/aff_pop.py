import matplotlib.pyplot as plt
from load_csv import load


def main():
    """This program will display population total and projection
    for France and Mali"""

    try:
        data = load("population_total.csv")
        assert data is not None, "No data provided"
        df = data.iloc(data.index.get_loc('France'),
                       data.index.get_loc('Mali')).set_index('country')
        print(df) 
        df = df.iloc[:, :df.columns.get_loc('2050')]
    
        print(df) 

        df.T.plot(kind='line',
                         title='France Life expectancy Projections',
                         ylabel='life expectancy', xlabel='year')
        plt.show()
        plt.close()
  
    except Exception as e:
        print("Error:", str(e), )

if __name__ == "__main__":
    main()
