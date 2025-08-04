#  Tweets Data Analysis

This project focuses on analyzing tweets from various sources, with an emphasis on identifying antisemitic content.

The goal is to extract insights from tweet texts about the use of antisemitic terminology online, such as:
- Number of antisemitic tweets
- Most common keywords
- Basic statcistical analysis



##  What Does the Project Do?

- **Reads Twitter files** (e.g., JSON/CSV) – Currently uses a built-in CSV file  
  The loading is handled in `load_file.py`  
  File path: `data/tweets_dataset.csv`

- **Performs text analysis using `pandas`** – Handled in `data_analyzer.py`  
  The script performs:
  1. Splits the dataset by category: antisemitic / non-antisemitic / other
  2. Calculates the average number of words per tweet by category and overall
  3. Finds the 3 longest tweets (in characters) per category
  4. Extracts the 10 most common words in all text
  5. Counts the number of fully-uppercase words (often indicating shouting)

- **Exports results to a JSON file** – Performed in `writes_to_json.py`

- **Cleans and rewrites the dataset** – Handled in `cleaner.py` under the `data/` folder


##  Main Tools and Libraries

- Python
- pandas
- json




