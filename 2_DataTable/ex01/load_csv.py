import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    try:
        data = pd.read_csv(path)
        print("Loading dataset of dimensions", data.shape)
        return (data)
    except Exception as e:
        print("Error:", str(e))
        return None
