import os
import numpy as np
import pandas as pd
#import matplotlib.pylot as plt

from get_movies import get_moviedata


movie_data = get_moviedata()

#not all films been interacted with every user. fill values with 0
item_matrix = movie_data.pivot(index=['userId'], columns =['movieId'],values='rating').fillna(0)

print(item_matrix)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#print(item_matrix.iloc[:,0])

def compute_movie_similarity_matrix(user_movie_matrix):
    n_movies = user_movie_matrix.shape[1]
    #print(n_movies)
    similarity_matrix = np.zeros((n_movies, n_movies))
    #print("Similarity matrix")
    print(similarity_matrix)
    print("going in loop")
    for i in range(n_movies):
        for j in range(i, n_movies):
            similarity = cosine_similarity(user_movie_matrix.iloc[:, i], user_movie_matrix.iloc[:, j])
            similarity_matrix[i, j] = similarity
            similarity_matrix[j, i] = similarity
    return similarity_matrix

similar = compute_movie_similarity_matrix(item_matrix)

print(similar)

#print(similar)








