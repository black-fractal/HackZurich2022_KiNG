from inference import predict_cluster
import nltk
import re
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
import re
from nltk.stem import WordNetLemmatizer 


# def tokenize_only(text):
#     # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
#     tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
#     filtered_tokens = []
#     # print(tokens)
#     # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
#     for token in tokens:
#         if re.search('[a-zA-Z]', token):
#             filtered_tokens.append(token)
#     # print(filtered_tokens)
#     return filtered_tokens

data_point={'name': 'Michael Delker',
 'interests': 'movie,adventure,science,politics,fashion,culture',
 'journey_frequency': 702,
 'cluster': None}

print('predict cluster')
print(predict_cluster([data_point['interests']])) 