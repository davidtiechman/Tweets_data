from src.LoadFile import load_file
class Cleaner():
    def __init__(self):
        self.df = load_file()
    def Toupper(self):
        self.df = load_file()
        self.df['Text'] = self.df['Text'].str.lower()
        return self.df
    def delete_non_biased(self):
        self.df = self.df[self.df['Biased'].notna()]
        return self.df
clean_df = Cleaner()
clean_df.Toupper()
clean_df.delete_non_biased()
print(clean_df.df.head())