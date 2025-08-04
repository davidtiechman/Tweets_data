import json
from unittest import result

from src.Data_analyzer import Analyzer


class WritesToJson:
    def __init__(self):
        self.analyzer = Analyzer()
    def write_to_json(self):
        result = {'total_tweets :': self.analyzer.Category_division(),
        'average_length :' : self.analyzer.Average_tweets_by_category(),
        'longest_three_tweets :': self.analyzer.Tweets_with_most_text(),
        'common_words :' : self.analyzer.Most_common_words(),
        'uppercase_words :' : self.analyzer.Words_with_capital()
       }
        with open('../data/results.json','a') as json_file:
            json.dump(result,json_file,indent=4)

# writes = WritesToJson()
# writes.write_to_json()
