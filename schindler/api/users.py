import random
import re

import names
import nltk
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
import re

from nltk.stem import WordNetLemmatizer

from schindler.ML.inference import *
from schindler.models import MAX_JOURNEY_FREQ, Cluster, UserProfile, interests


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

def generate_random_users(number):
    users = []
    for _ in range(number):
        try:
            users.append(generate_random_user())
        except Exception as e:
            print(e)

    return users


def generate_random_user():
    user_interests = ','.join([interest for interest, _ in random.sample(interests, random.randint(1, 7))])

    c1 = Cluster( label=calculate_cluster( user_interests ) )
    c1.save()
    
    user = UserProfile(name=names.get_full_name(), journey_frequency=random.randint(0, MAX_JOURNEY_FREQ),
                       interests=user_interests, cluster=c1)
    user.interests = user_interests

    user.save()

    return user.to_json()

def calculate_cluster( list_of_interests ):
    return predict_cluster( [list_of_interests] )