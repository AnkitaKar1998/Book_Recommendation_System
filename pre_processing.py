import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

def collaborative_preprocess():
    data = pd.read_csv(r'datasets/collaborative_dataset.csv')
    knn_table = data.pivot_table(index='ISBN', columns='User_ID', values='Book_Rating').fillna(0)
    pearson_table = data.pivot_table(index='User_ID', columns='ISBN', values='Book_Rating').fillna(0)
    return knn_table, pearson_table

def content_based_preprocess():
    data = pd.read_csv(r'datasets/content_dataset.csv')
    vectorizer = CountVectorizer()
    cm = vectorizer.fit_transform(data['Important_Features'])
    cosine_matrix = cosine_similarity(cm)
    return cosine_matrix

def get_popular_books():
    data = pd.read_csv(r'datasets/popular_books.csv')
    data.drop(data.columns[[0]], axis=1, inplace=True)
    initial_data = []
    for i in range(data.shape[0]):
        initial_data.append(dict(data.loc[i]))
    return initial_data


def get_all_books():
    data = pd.read_csv(r'datasets/content_dataset.csv')
    data.drop(data.columns[[0]], axis=1, inplace=True)
    initial_data = []
    for i in range(data.shape[0]):
        initial_data.append(dict(data.loc[i]))
    return initial_data
