import os
import numpy as np
import pandas as pd
#import matplotlib.pylot as plt

from get_movies import get_moviedata


movie_data = get_moviedata()
unique_titles = movie_data['title'].unique()
#print(len(unique_titles))
#print(len(list(movie_data['title'])))

#not all films been interacted with every user. fill values with 0
item_matrix = movie_data.pivot(index=['userId'], columns =['movieId'],values='rating').fillna(0)

#print(item_matrix)

movie_ids = item_matrix.columns.tolist()

#print(movie_ids)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

#print(item_matrix.iloc[:,0])

movie_id_to_similarity = {}

def compute_movie_similarity_matrix(user_movie_matrix):
    n_movies = user_movie_matrix.shape[1]
    similarity_matrix = np.zeros((n_movies, n_movies))
    #print(similarity_matrix)
    print("going in loop")
    for i in range(n_movies):
        movie_id_to_similarity[movie_ids[i]] = i
    for i in range(n_movies):
            for j in range(i, n_movies):
                similarity = cosine_similarity(user_movie_matrix.iloc[:, i], user_movie_matrix.iloc[:, j])
                similarity_matrix[i, j] = similarity
                similarity_matrix[j, i] = similarity
    return similarity_matrix

compute_movie_similarity_matrix(item_matrix)
print(movie_id_to_similarity)


def get_k_similar_movies(movie_similarity_matrix, movie_index, k):
    movie_similarities = movie_similarity_matrix[movie_index]
    return np.argsort(movie_similarities)[-k-1:-1][::-1]

def get_movie_based_recommendations(user_movie_matrix, movie_titles, input_movie,k=10, n_recommendations=5):
    movie_similarity_matrix = compute_movie_similarity_matrix(user_movie_matrix)

    try:
        movie_index = movie_titles.index(input_movie)
    except ValueError:
        return "Movie not found in database."

    similar_movies_indicies = get_k_similar_movies(movie_similarity_matrix, movie_index, k)


    similar_movies = [movie_titles[i] for i in similar_movies_indicies]

    similarity_scores = movie_similarity_matrix[movie_index, similar_movies_indicies]

    recommendations = pd.DataFrame({
        'Movie': similar_movies,
        'Similarity Score': similarity_scores
    })

    return recommendations.sort_values('Similarity Score', ascending=False).head(n_recommendations)





#similar = compute_movie_similarity_matrix(item_matrix)

#print(similar)

#print(similar)








