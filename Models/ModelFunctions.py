import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors


# TODO: Assign X as pandas dataframe when sql db data is loaded
# songs_df =  ... our sql db as a pandas df
# y = songs_df[songs_df.columns[1]] # y is our song id
# X = songs_df[songs_df.columns[3:]] # X is our song attributes ('danceability', 'energy', etc.)
# X and y are as written global variables and that is assumed in the definitions below,
# this may need to change later on if we determine we don't want these to be global

def preprocess(df):
    """ normalizes pandas df.
    Removes unecessary columns """
    drop_cols = ['duration_ms', 'key', 'mode', 'time_signature', 'popularity','tempo']
    df = df.drop(columns=drop_cols)
    scaler = MinMaxScaler()
    scaler.fit_transform(df)
    return df

def create_model(X, n_neighbors=10)
    """ Insantiate nearest neighbor model """
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='kd_tree')
    model.fit(X)
    return model

def suggest_songs(source_song, model):
    """ Preprecesses source song, use it to make suggestions from the database """
    source_song = preprocess(source_song)
    recommendations = nn.kneighbors(source_soung)[1][0]
    recommendations_dict = y.iloc[recommendations].T.to_dict()
    return recommendations_dict
