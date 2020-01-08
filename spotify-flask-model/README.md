
# tested in jupyter notebook

# local url
url = 'http://127.0.0.1:5000'

# test data
data = """
{"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O",
"track_name":"Big Bank feat. 2 Chainz, Big Sean,Nicki Minaj",
"acousticness":0.00582,"danceability":0.743,"duration_ms":238373,
"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,
"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,
"time_signature":4,"valence":0.118,"popularity":15}
"""

import requests 
r_survey = requests.post(url, data)
print(r_survey)


send_request = requests.post(url, data)
print(send_request)

print(send_request.json())

{'results': {'results': '       artist_name                track_id                                        track_name\n0               YG  2RM4jf1Xa9zPgMGRDiht8O    Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj\n123910          YG  0ZNrc4kNeQYD9koZ3KvCsy  BIG BANK (feat. 2 Chainz, Big Sean, Nicki Minaj)'}}