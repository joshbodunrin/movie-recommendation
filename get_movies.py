import os
import numpy as np
import pandas as pd
#import matplotlib.pylot as plt


ratings_df = pd.read_csv("../archive/ratings_small.csv")

metadata_df = pd.read_csv("../archive/movies_metadata.csv", low_memory=False)

#print(list(ratings_df.columns))

#print(list(metadata_df.columns))

metadata_df['id'] = pd.to_numeric(metadata_df['id'], errors='coerce')

metadata_df = metadata_df.dropna(subset=['id'])

metadata_df['id'] = metadata_df['id'].astype('int64')
moviedata_df = pd.merge(ratings_df,metadata_df, left_on='movieId',right_on='id')

moviedata_df = moviedata_df[['userId','movieId','rating','timestamp','genres','id','popularity','title','vote_average','vote_count']]

moviedata_df = moviedata_df.dropna()


print(list(moviedata_df.columns))

print(moviedata_df)


