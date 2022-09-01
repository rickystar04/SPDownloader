from modules.metadata import *
from modules.convert import *
from pytube import YouTube
from urllib.parse import urlparse
import urllib.request
import re
import os
from modules.spotify import *
from modules.banner import *
from modules.color import *



os.system('cls' if os.name == 'nt' else 'clear')
banner()

if(not os.path.exists("music")):
	os.mkdir("music")

if(not os.path.exists("images")):
	os.mkdir("images")

while True:
	playlist_id=input("Inserisci link playlist: ")
	
	run(playlist_id)
	
	if(input("E' la playlist giusta? [y/n] >>> ")=="y"):
		playlist_name=correct(playlist_id)
		break
		
title_list=open("tracks_title.txt", "r")
artist_list=open("tracks_artist.txt", "r")
album_list=open("tracks_album.txt", "r")
i=0

with open("tracks_list.txt") as file:
	for line in file:
		query=urllib.parse.quote(line.rstrip()+" lyrics")
		
		url="https://www.youtube.com/results?search_query="+query

		html=urllib.request.urlopen(url)

		link=re.findall(r"watch\?v=(\S{11})", html.read().decode())

		url="https://www.youtube.com/watch?v="+link[0]
		
		yt=YouTube(url)

		yt.streams.first().download("music/"+playlist_name)

		file_name=yt.streams.first().default_filename
		
		os.rename("music/"+playlist_name+"/"+file_name, "music/"+playlist_name+"/"+yt.streams.first().title)

		file_name=yt.streams.first().title
		
		print(file_name)
		
		title=title_list.readline().strip()
		artist=artist_list.readline().strip()
		album=album_list.readline().strip()
		
		path("music/"+playlist_name+"/"+file_name, playlist_name, title+".mp3")
		
		image(title, artist, album, playlist_name)
		
		print("\033[0;32m	[✓]"+title+" successfully downloaded\033[0m")
		i+=1

title_list.close()
artist_list.close()
album_list.close()

os.remove("tracks_title.txt")
os.remove("tracks_list.txt")
os.remove("tracks_artist.txt")
os.remove("tracks_album.txt")
dir = 'images/'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
