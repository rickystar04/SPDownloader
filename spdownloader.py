import re
import os
import sys

# import ffmpeg
from pytube import YouTube
from modules.metadata import *
from modules.spotify import *
from modules.banner import *
from modules.color import *
from modules.cred import *
from modules.download_thread import *
from modules.manage_spotify import *
import urllib.request


def start_download(playlist_name, type):
    with open("records.json", "r") as file:
        records = json.load(file)
    file.close()

    if isinstance(records, list):
        count = len(records)
    elif isinstance(records, dict):
        count = len(records.keys())
    else:
        count = 0
    print("COUNT: " + str(count))
    for record in records:
        title = record["titolo"]
        artist = record["artista"]

        exist = os.path.isfile("music/" + playlist_name + "/" + title + ".mp3")

        if not exist:
            query = urllib.parse.quote(title + artist + " lyrics")

            url = "https://www.youtube.com/results?search_query=" + query

            record["song_link"] = str(url)

    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)
    file.close()

    thread(playlist_name, count)
    image(playlist_name, type)

    print(color.BOLD + color.RED + "\nFinished!" + color.END)
    #


    dir = "images/"
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    os.remove("records.json ")


def main():

    exist = os.path.isfile(".env.example")
    if(exist):
        if os.name == 'nt':  # Windows
            cmd = f'copy .env.example .env'
        else:  # Unix/Linux
            cmd = f'cp "{src}" "{dst}"'
        os.system(cmd)
    
    cycle = True
    while cycle:
        
        os.system("cls" if os.name == "nt" else "clear")
        banner(0.03)
        if not os.path.exists("music"):
            os.mkdir("music")

        if not os.path.exists("images"):
            os.mkdir("images")

        auth = checkAuth()
        if auth:
            link = input("Paste playlist link: ")

            name, type = song_download(link)
            if type == "playlist":
                print("PLAYLIST: " + name)

            elif type == "album":
                print("ALBUM: " + name)

            cycle = False
            if input("Is this the right " + type + "?? [y/n] >>> ") == "y":
                start_download(name, type)

            else:
                os.system("cls" if os.name == "nt" else "clear")
                banner(0)
        else:
            verify_credential()
            cycle=False
if __name__ == "__main__":
    main()
