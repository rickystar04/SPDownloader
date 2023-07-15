import json
import os
import re
import urllib.request

import yt_dlp

from modules import spotify
from modules.banner import banner
from modules.color import color
from modules.metadata import image

# try:
os.system("cls" if os.name == "nt" else "clear")
banner(0.03)

if not os.path.exists("music"):
    os.mkdir("music")

if not os.path.exists("images"):
    os.mkdir("images")

while True:
    playlist_id = input("Paste playlist link: ")

    spotify.run(playlist_id)

    if input("Is this the right playlist?? [y/n] >>> ") == "y":
        playlist_name = spotify.correct(playlist_id)
        break
    else:
        os.system("cls" if os.name == "nt" else "clear")
        banner(0)

title_list = open("tracks_title.txt", "r")
artist_list = open("tracks_artist.txt", "r")
album_list = open("tracks_album.txt", "r")
i = 0

with open("tracks_list.txt") as file:
    for line in file:
        i += 1

        query = urllib.parse.quote(line.rstrip() + " lyrics")

        url = "https://www.youtube.com/results?search_query=" + query

        html = urllib.request.urlopen(url)

        link = re.findall(r"watch\?v=(\S{11})", html.read().decode())

        url = f"https://www.youtube.com/watch?v={link[0]}"

        title = title_list.readline().strip()
        print(f"Title: {title}")

        ydl_opts = {
            "format": "mp3/bestaudio/best",
            "outtmpl": f"/music/{playlist_name}/%(title)s.%(ext)s",
            "postprocessors": [
                {  # Extract audio using ffmpeg
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                }
            ],
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            error_code = ydl.download(url)

        artist = artist_list.readline().strip()
        album = album_list.readline().strip()

        image(info["title"], title, artist, album, playlist_name)

        total_songs = len(title_list.readlines()) + 1
        print(
            f"{color.GREEN}[✓ {i}/{total_songs}]{color.BOLD}{title}{color.END}{color.GREEN} successfully downloaded\033[0m"
        )
# except Exception as err:
# print(err)
# print(f"{color.RED} SOMETHING HAS GONE WRONG TRY AGAIN LATER...")

# TODO
# with open("track.json", 'r') as file:
#     data = json.load(file)
#     for item in data["Playlist"]:
#         item["album"]

# finally:
title_list.close()
artist_list.close()
album_list.close()

os.remove("tracks_title.txt")
os.remove("tracks_list.txt")
os.remove("tracks_artist.txt")
os.remove("tracks_album.txt")
dir = "images/"
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

print(color.BOLD + color.PURPLE + "\nFinished!" + color.END)
