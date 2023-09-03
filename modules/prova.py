import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="ae49e6be16674c81a0ebdb8f68fcc029",
        client_secret="e4503a68d1ee42f59595362825fc411d",
    )
)

results = sp.search(q="weezer", limit=20)
for idx, track in enumerate(results["tracks"]["items"]):
    print(idx, track["name"])
