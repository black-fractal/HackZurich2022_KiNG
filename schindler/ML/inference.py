# -*- coding: utf-8 -*-
"""Inference.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yJ-cmLuKCHfDVXzXgqGpXrprDh-HJ9jL
"""

import json
import os
import time
from copy import deepcopy

# Commented out IPython magic to ensure Python compatibility.
import joblib
# viz
import matplotlib.pyplot as plt
import nltk
import numpy as np
# data
import pandas as pd
from nltk.stem import WordNetLemmatizer
from scipy.cluster.hierarchy import (complete, dendrogram, fcluster, single,
                                     ward)
from scipy.spatial import distance
from sklearn.cluster import KMeans
# feature extraction
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score
from sklearn.metrics.pairwise import cosine_similarity
# other
from tqdm import tqdm

# %matplotlib inline



nltk.download('wordnet')
nltk.download('punkt')

from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
import re


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    print(tokens)
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems


def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # print(tokens)
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    # print(filtered_tokens)
    return filtered_tokens

def load_models(Path_Kmeans, Path_tfidf):
  km = joblib.load(Path_Kmeans)
  tfidf_vec = joblib.load(Path_tfidf)
  return km,tfidf_vec



def predict_cluster(data):
  km_model,tfidf_model=load_models('/home/ubuntu/hackzurich/HackZurich2022_KiNG/schindler/ML/Models/Km_model.joblib',  '/home/ubuntu/hackzurich/HackZurich2022_KiNG/schindler/ML/Models/tfidf_vector_model.joblib')
  tfidf_matrix = tfidf_model.transform(data)
  lables= km_model.predict(tfidf_matrix)
  return lables[0]

def find_nearset_cluster(data_clusters):
  km_model,tfidf_model=load_models('/home/ubuntu/hackzurich/HackZurich2022_KiNG/schindler/ML/Models/Km_model.joblib',  '/home/ubuntu/hackzurich/HackZurich2022_KiNG/schindler/ML/Models/tfidf_vector_model.joblib')
  df_cluster_mapping = pd.read_csv('/home/ubuntu/hackzurich/HackZurich2022_KiNG/schindler/ML/Clustered Data/cluster_mapping_.csv')
  if len(np.unique(data_clusters))==1:
    return np.unique(data_clusters)
  else:
    centers=  km_model.cluster_centers_ 
    centroids_midpoint=np.zeros((len(centers[0])))
    
    for val in np.unique(data_clusters):
      for i in range (len(centers[0])):
        centroids_midpoint[i] += centers[val][i]
    centroids_midpoint=centroids_midpoint/len(np.unique(data_clusters))
    distances=[]
    for i in range(len(centers)):
      distances.append(distance.euclidean(centroids_midpoint, centers[i]))
    return  df_cluster_mapping[df_cluster_mapping['Cluster']==np.argmin(np.array(distances))]['Interests'].values

# data_point={'name': 'Michael Delker',
#  'interests': 'movie,adventure,science,politics,fashion,culture',
#  'journey_frequency': 702,
#  'cluster': None}

# print('predict cluster')
# print(predict_cluster([data_point['interests']]))

