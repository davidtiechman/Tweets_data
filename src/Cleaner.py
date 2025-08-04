from src.LoadFile import load_file
class Cleaner:
    def __init__(self):
        self.df = load_file()
    def Toupper(self):
        self.df = load_file()
        self.df['Text'] = self.df['Text'].str.lower()
        return self.df
    def delete_non_biased(self):
        self.df = self.df[self.df['Biased'].notna()]
        return self.df
    def Export_a_new_file(self):
        self.df.to_csv('../data/tweets_dataset_cleaned.csv', index=False)
