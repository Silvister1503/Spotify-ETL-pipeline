import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    playlists = sp.user_playlists('spotify')
    
    Playlist_Link = "https://open.spotify.com/playlist/4nNVfQ9eWidZXkBKZN5li4"
    Playlist_URI = Playlist_Link.split("/")[-1]
    
    spotify_data = sp.playlist_tracks(Playlist_URI)

    cilent = boto3.client('s3')
    
    filename = "spotify_raw_" + str(datetime.now()) + ".json"
    
    cilent.put_object(
        Bucket="spotify-s3-bucket-sameer",
        Key="raw_data/to_be_processed/" + filename,
        Body=json.dumps(spotify_data)
        )