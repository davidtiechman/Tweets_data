from collections import Counter
from src.LoadFile import load_file

df = load_file()
# כמה ציוצים יש מכל קטגוריה )לפי קטגוריה, לא מוגדר, וסה"כ(
# catego =  df['Biased'].value_counts()
# total = catego.sum()
# print(catego[0])
# print(catego[1])
# print(total)
# # מה האורך הממוצע )במילים( של ציוצים )לפי קטגוריה וסה"כ(
df['len_text'] = df['Text'].str.len()
# mean_catego = df.groupby("Biased")['len_text'].mean()
# print(mean_catego[0])
# print(mean_catego[1])
# print(df['len_text'].mean())
# מהם 3 הציוצים עם כמות המלל הגדולה ביותר )לפי קטגוריה(
df_sort_0 =df[df['Biased'] == 0]
df_sort_1 =df[df['Biased'] == 1]
# print(df_sort_0.sort_values('len_text', ascending=False)['len_text'].head(3))
# print(df_sort_1.sort_values('len_text', ascending=False)['len_text'].head(3))
# מהם 10 המילים הנפוצות ביותר בכל הציוצים )מכל הקטגוריות(
# print(df.sort_values('Text').mode().head(10))
# df_null = df[df['len_text'] == 'null']
df['array_text'] = df['Text'].str.split(" ")
df['array_text'].head()
# df['len_words'] = df['array_text'].apply(lambda x: len(x))
df['len_words'] = df['array_text'].str.len()
# df['array_text'].mode())
# print(df['len_words'].max())
# print(df['len_text'].max())
# all_words = sum(df['array_text'],[])
# conter = Counter(all_words)
# print(conter.most_common(10))
df['sum_lower'] = df['array_text'].apply(lambda word_list: sum(word.isupper()for word in word_list))
print(df.groupby('Biased')['sum_lower'].sum())
print(df['sum_lower'].sum())
