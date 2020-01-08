
# test on heroku in jupyter notebook

# set url 
```
url = 'https://spotify-flask-model.herokuapp.com/' 
# or use 'http://127.0.0.1:5000' to test locally
```

# test sample data
```
data = """
{"artist_name":"YG","track_id":"2RM4jf1Xa9zPgMGRDiht8O",
"track_name":"Big Bank feat. 2 Chainz, Big Sean,Nicki Minaj",
"acousticness":0.00582,"danceability":0.743,"duration_ms":238373,
"energy":0.339,"instrumentalness":0.0,"key":1,"liveness":0.0812,
"loudness":-7.678,"mode":1,"speechiness":0.409,"tempo":203.927,
"time_signature":4,"valence":0.118,"popularity":15}
"""
```
# check server response
```
import requests 
r_survey = requests.post(url, data)
print(r_survey)
```
```
 <Response [200]>
```

```
send_request = requests.post(url, data)
print(send_request)
```

```
<Response [200]>
```
# get predictions 
```
print(send_request.json())
```

```
{'results': {'results': '            artist_name                track_id                                        track_name\n0                    YG  2RM4jf1Xa9zPgMGRDiht8O    Big Bank feat. 2 Chainz, Big Sean, Nicki Minaj\n123910               YG  0ZNrc4kNeQYD9koZ3KvCsy  BIG BANK (feat. 2 Chainz, Big Sean, Nicki Minaj)\n43679   Malcolm Anthony  2BhNdsWlcpHeJGM85EjOlO                                           My Town\n15960            SG Tip  31cZdDNDDvmPDfBUT1zYFf                                          No Brain\n40897           Joell B  7bsBenFEDBYMkA5D0Bvwww                                            Trauma\n110212           REASON  274Dih3HQsnMt9aJputs7N                                            Bottom\n49275        Jose Guapo  4MifHoD1ugjZXg3uDDvEbH                                 How to Get a Sack\n125047       Gucci Mane  0sM8ktJMFE7yCY4sWucgyQ                                         By Myself\n211           Money Man  2jCPVc4w44ZjcFDFsPy1i0                                             Picky\n101642      ScHoolboy Q  4dTiQezDWmEOWcdCbWVWMp                                   Numb Numb Juice'}}
```