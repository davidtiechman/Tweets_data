from collections import Counter
from src.LoadFile import load_file
class Analyzer():
    def __init__(self):
        self.df = load_file()

# כמה ציוצים יש מכל קטגוריה )לפי קטגוריה, לא מוגדר, וסה"כ(
    def Category_division(self):
        category =  self.df['Biased'].value_counts()
        total = category.sum()
        dict = {'total_tweets': {
            'antisemitic': int(category[1]),
            'non antisemitic': int(category[0]),
            'total':int(total)
        }}
        return dict

# # מה האורך הממוצע )במילים( של ציוצים )לפי קטגוריה וסה"כ(
    def Average_tweets_by_category(self):
        self.df['array_text'] = self.df['Text'].str.split(" ")
        self.df['count_words'] = self.df['array_text'].apply(lambda x: len(x))
        mean_catego = self.df.groupby("Biased")['count_words'].mean()
        average_total_by_words = self.df['count_words'].mean()
        dict = {"average_length": {
        "antisemitic": int(mean_catego[1]),
        "non_antisemitic": int(mean_catego[0]),
        "total": int(average_total_by_words)
        }}
        return dict


# מהם 3 הציוצים עם כמות המלל הגדולה ביותר )לפי קטגוריה(
    def Tweets_with_most_text(self):
        self.df['len_text'] = self.df['Text'].str.len()
        df_by_biades_0 = self.df[self.df['Biased']==0]
        df_by_biades_1 = self.df[self.df['Biased']==1]
        most_text_by_0 = df_by_biades_0.sort_values('len_text', ascending=False)['Text'].head(3)
        most_text_by_1 = df_by_biades_1.sort_values('len_text', ascending=False)['Text'].head(3)
        dict = {
            'longest_3_tweets': {
                'antisemitic' :[str(most_text_by_0)],
                'non_antisetic' :[str(most_text_by_1)]
            }
        }
        return dict

# מהם 10 המילים הנפוצות ביותר בכל הציוצים )מכל הקטגוריות(
    def Most_common_words(self):
        # משטח את כל המערכים של כל רשומה לרשימה אחת גדולה
        all_words = sum(self.df['array_text'],[])
        # עושה מיליון מכל מילה ברשימה לפי כמה פעמים הוא נמצא
        conter = Counter(all_words)
        # מחזיר את ה 10 המילים הכי נפוצים
        dict = {'common_words': [conter.most_common(10)]}
        return dict

# כמה מילים באותיות גדולות )לפי קטגוריה וסה"כ( ]הארה: מאפיין צעקות[
    def Words_with_capital(self):
        self.df['sum_upper'] = self.df['array_text'].apply(lambda word_list: sum(word.isupper() for word in word_list))
        dict = {
            'uppercase_words' : {
                'antisemitic' : str(self.df['sum_upper']),
                'non_antiset(ic' : str(self.df['sum_upper']),
                'total' :str( self.df['sum_upper'])
            }
        }
        return dict

# analyzer = Analyzer()
# print(analyzer.Category_division())
# print(analyzer.Average_tweets_by_category())
# print(analyzer.Tweets_with_most_text())
# analyzer.Most_common_words()
# analyzer.Words_with_capital()