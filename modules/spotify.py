import spotipy
from spotipy.oauth2 import SpotifyOAuth
import urllib.request 
from .color import color
from . import cred
import os




scope = "playlist-read-private"
try:
	sp=spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID, client_secret= cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))

except spotipy.oauth2.SpotifyOauthError as e:
	print("Errore nell'autenticazione")

def run(playlist_id):
	playlist_id=playlist_id

	playlist_URI=playlist_id.split("/")[-1].split("?")[0]

	playlist_name=sp.playlist(playlist_URI)
	results=sp.playlist_tracks(playlist_URI)

	tracks = results['items']

	while results['next']:
		results = sp.next(results)
		tracks.extend(results['items'])

	i=0
	f=open("tracks_list.txt", "w")
	f2=open("tracks_title.txt", "w")
	f3=open("tracks_artist.txt", "w")
	f4=open("tracks_album.txt", "w")
	
	playlist_name=playlist_name["name"]
	print("\nPlaylist: "+color.CYAN+playlist_name+color.END)

	for track in tracks:
		i+=1
		print(color.BLUE+"["+str(i)+"]"+color.END+" "+track['track']['name']+" - "+track["track"]["artists"][0]["name"])
		
		track_name=track['track']['name']
		track_artist=track["track"]["artists"][0]["name"]
		track_album=track['track']['album']["name"]

		f.write(track_name+" - "+track_artist+"\n")
		f2.write(track_name+"\n")
		f3.write(track_artist+"\n")
		f4.write(track_album+"\n")

		image_link=track["track"]["album"]["images"][0]["url"]
	f.close()

def correct(playlist_id):
	playlist_id=playlist_id

	playlist_URI=playlist_id.split("/")[-1].split("?")[0]

	playlist_name=sp.playlist(playlist_URI)
	results=sp.playlist_tracks(playlist_URI)

	tracks = results['items']

	playlist_name=playlist_name["name"]

	if(not os.path.exists("./music/"+playlist_name)):
		os.mkdir("music/"+playlist_name)

	while results['next']:
		results = sp.next(results)
		tracks.extend(results['items'])

	i=0
	for track in tracks:
		i+=1
		track_name=track['track']['name']
		image_link=track["track"]["album"]["images"][0]["url"]
		
		img=open("images/"+track_name+" cover.jpg", "wb")
		img.write(urllib.request.urlopen(image_link).read())
		img.close()
	return playlist_name
