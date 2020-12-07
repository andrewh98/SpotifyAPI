import requests
import json
import base64

client_id = '40d5bd41416e48c29cf3f8aac94b6682'
client_secret = '**************************'

def getAccessToken(client_id, client_secret):
    # encode client_id and client_secret into base64
    client_creds = f'{client_id}:{client_secret}'
    client_creds_b64 = base64.b64encode(client_creds.encode())

    # curl -X "POST" -H "Authorization: Basic ZjM4ZjAw...WY0MzE="
    # -d grant_type=client_credentials https://accounts.spotify.com/api/token
    endpoint = 'https://accounts.spotify.com/api/token'
    token_data = {'grant_type': 'client_credentials'}
    token_headers = {'Authorization': f'Basic {client_creds_b64.decode()}'}

    r = requests.post(endpoint, headers=token_headers, data=token_data)
    response = r.json()
    #print(json.dumps(response, indent=4))
    accessToken = response['access_token']
    return accessToken

def getTrack(token, track_id):
    # curl -X "GET" "https://api.spotify.com/v1/tracks/11dFghVXANMlKmJXsNCbNl?market=ES"
    # -H "Accept: application/json"
    # -H "Content-Type: application/json" -H "Authorization: Bearer "

    track_endpoint = f'https://api.spotify.com/v1/tracks/{track_id}'
    track_header = {'Authorization': 'Bearer ' + token}

    r = requests.get(track_endpoint, headers=track_header)
    track_info = r.json()
    return track_info


token = getAccessToken(client_id, client_secret)
track_id = '3n3Ppam7vgaVa1iaRUc9Lp'

track_list = getTrack(token, track_id)
# print(json.dumps(track_list, indent=4))

for t in track_list['album']['artists']:
    trackName = (t['name'])
    print(trackName)
