import pandas as pd
from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

infile = "https://raw.githubusercontent.com/spotify-recommendation-engine-3/data_science/master/Data/SpotifyAudioFeaturesApril2019_duplicates_removed.csv"
songs_df = pd.read_csv(infile)
y = songs_df[songs_df.columns[:3]]
X = songs_df[songs_df.columns[3:]]

test_song = {"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O","track_name":"Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj","acousticness":0.00582,"danceability":0.743,"duration_ms":238373,"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,"time_signature":4,"valence":0.118,"popularity":15}

def preprocess(df):
    """ normalizes pandas df.
    Removes unecessary columns """
    drop_cols = ['duration_ms', 'key', 'mode', 'time_signature', 'popularity','tempo']
    df = df.drop(columns=drop_cols)
    scaler = MinMaxScaler()
    scaler.fit_transform(df)
    return df

def create_model(X, n_neighbors=10):
    """ Insantiate nearest neighbor model """
    model = NearestNeighbors(n_neighbors=n_neighbors, algorithm='kd_tree')
    model.fit(X)
    return model

def suggest_songs(source_song, model):
    """ Preprecesses source song, use it to make suggestions from the database """
    source_song = preprocess(source_song)
    recommendations = model.kneighbors(source_song)[1][0][1:] #remove 1st result (source)
    recommendations_dict = y.iloc[recommendations].T.to_dict()
    return recommendations_dict

my_model = create_model(preprocess(X))

@app.route('/pred', methods=['GET'])
def returnAll():
    song_dict = {"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O","track_name":"Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj","acousticness":0.00582,"danceability":0.743,"duration_ms":238373,"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,"time_signature":4,"valence":0.118,"popularity":15}
    song_dict.update((x, [y]) for x, y in song_dict.items())
    song_df = pd.DataFrame.from_dict(song_dict)
    song_df = song_df[song_df.columns[3:]]

    
    result = suggest_songs(song_df, my_model)

    return jsonify(result)

@app.route('/pred', methods=['POST'])
def runPred():
    
    input_song = request.get_json(force=True)
    input_song.update((x, [y]) for x, y in input_song.items())

    song_df = pd.DataFrame.from_dict(input_song)
    song_df = song_df[song_df.columns[3:]]
    
    results = suggest_songs(song_df, my_model)

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
