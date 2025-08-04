import pandas as pd
def load_file():
    df = pd.read_csv('../data/tweets_dataset.csv')
    return df
