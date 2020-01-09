import pandas as pd
from flask import Flask, jsonify, request
import json

from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import NearestNeighbors


df = pd.read_csv('SpotifyAudioFeaturesApril2019.csv')

# Separate data into features and targets
# target is the first 3 columns, ie. artist, song_id, and song name
target = df.columns[:3] 
features = df.columns[3:]

X = df[features]
y = df[target]

# remove potentially unecessary columns
drop_cols = ['duration_ms', 'key', 'mode', 'time_signature', 'popularity','tempo'] 
X = X.drop(columns=drop_cols)

# scaling 
scaler = MinMaxScaler()
scaler.fit_transform(X)

# model 
model = NearestNeighbors(n_neighbors=10, algorithm='kd_tree')
model.fit(X)

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])

def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into series # try json.loads else
    labels = ['artist_name', 'track_id', 'track_name', 'duration_ms', 'key', 'mode', 'tempo', 'time_signature', 'popularity']      
    predictor = pd.Series(json.loads(data)).drop(labels=labels)
    
    # predictions
    recommendations = model.kneighbors([predictor])[1][0]
    
    # send back to browser
    output = {'results': str(y.iloc[recommendations][:10])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    app.run(port = 5000, debug=True)

