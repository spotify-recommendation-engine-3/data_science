import pandas as pd
import pdb
from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

infile = "https://raw.githubusercontent.com/Tclack88/Machine-Learning-Projects/master/SpotifyAudioFeaturesApril2019.csv"
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
    pdb.set_trace()
    recommendations = model.kneighbors(source_song)[1][0]
    
    recommendations_dict = y.iloc[recommendations].T.to_dict()
    return recommendations_dict

@app.route('/pred', methods=['GET'])
def returnAll():
    derp_dict = {"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O","track_name":"Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj","acousticness":0.00582,"danceability":0.743,"duration_ms":238373,"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,"time_signature":4,"valence":0.118,"popularity":15}
    derp_dict.update((x, [y]) for x, y in derp_dict.items())
    song_df = pd.DataFrame.from_dict(derp_dict)
    song_df = song_df[song_df.columns[3:]]

    my_model = create_model(preprocess(X))
    result = suggest_songs(song_df, my_model)

    # song_df = song_df.to_dict()

    # result = suggest_songs(song_df, model)

    return jsonify(result)

@app.route('/pred', methods=['POST'])
def runPred():
    # input_song = request.get_json(force=True)
    # input_song.update((x, [y]) for x, y in input_song.items())

    # test_song.update((x, [y]) for x, y in input_song.items())
    derp_dict = {"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O","track_name":"Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj","acousticness":0.00582,"danceability":0.743,"duration_ms":238373,"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,"time_signature":4,"valence":0.118,"popularity":15}

    song_df = pd.DataFrame.from_dict(derp_dict)

    result = suggest_songs(song_df, model)

    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
