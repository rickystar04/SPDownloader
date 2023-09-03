import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
import urllib.request
from .color import color
from . import cred
import os
import json


tracks = []

sp = ""


def playlist_download(playlist, results):
    type = "playlist"
    tracks = results["items"]

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    i = 0

    playlist_name = playlist["name"]
    print("Playlist: " + color.CYAN + playlist_name + color.END)

    records = []
    for track in tracks:
        i += 1
        print(
            color.BLUE
            + "["
            + str(i)
            + "]"
            + color.END
            + " "
            + track["track"]["name"]
            + " - "
            + track["track"]["artists"][0]["name"]
        )
        track_name = track["track"]["name"]
        track_artist = track["track"]["artists"][0]["name"]
        track_album = track["track"]["album"]
        image_link = track["track"]["album"]["images"][0]["url"]

        title_final = track_name.replace("/", "")
        title_final = title_final.replace('"', "")
        title = title_final.replace(".", "")
        record = {
            "titolo": title,
            "artista": track_artist,
            "album": track_album,
            "image": image_link,
        }
        records.append(record)

    # f.close()
    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)
    file.close()
    print("TIPO:" + type)
    return playlist_name, type


def album_download(album, results, image_link):
    type = "album"
    tracks = results["items"]

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    i = 0

    album_name = album["name"]
    print("Album: " + color.CYAN + album_name + color.END)

    records = []
    for track in tracks:
        i += 1
        print(
            color.BLUE
            + "["
            + str(i)
            + "]"
            + color.END
            + " "
            + track["name"]
            + " - "
            + track["artists"][0]["name"]
        )

        track_name = track["name"]
        track_artist = track["artists"][0]["name"]
        track_album = album_name

        # image_link = track["images"][0]["url"]
        title_final = track_name.replace("/", "")
        title_final = title_final.replace('"', "")
        title = title_final.replace(".", "")

        record = {
            "titolo": title,
            "artista": track_artist,
            "album": track_album,
            "image": image_link,
        }
        records.append(record)
    # f.close()

    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)
    file.close()
    return album_name, type


def checkAuth():
    global sp
    scope = "playlist-read-private"
    try:
        # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_ID,
        #                                               client_secret=cred.client_SECRET, redirect_uri=cred.redirect_url, scope=scope))
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id="ae49e6be16674c81a0ebdb8f68fcc029",
                client_secret="e4503a68d1ee42f59595362825fc411d",
                redirect_uri="http://localhost:9000",
                scope=scope,
            )
        )
        return True
    except spotipy.oauth2.SpotifyOauthError as e:
        print("Error during authentication: " + str(e))
        return False


def song_download(playlist_id):
    scope = "playlist-read-private"
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id="ae49e6be16674c81a0ebdb8f68fcc029",
            client_secret="e4503a68d1ee42f59595362825fc411d",
            redirect_uri="http://localhost:9000",
            scope=scope,
        )
    )
    print("3")
    playlist_id = playlist_id
    print("4")
    print(playlist_id)
    playlist_URI = playlist_id.split("/")[-1].split("?")[0]
    print(playlist_URI)
    print("5")
    try:
        playlist = sp.playlist(playlist_URI)
        print("6")
        results = sp.playlist_tracks(playlist_URI)
        print("7")

        return playlist_download(playlist, results)

    except Exception:
        try:
            album = sp.album(playlist_URI)
            print("8")
            results = sp.album_tracks(playlist_URI)
            print("9")
            image_link = album["images"][0]["url"]
            print(image_link)
            return album_download(album, results, image_link)
        except Exception as e:
            print("ERRORE: " + str(e))
            breakpoint


def correct(playlist_id):
    global sp
    playlist_id = playlist_id

    playlist_URI = playlist_id.split("/")[-1].split("?")[0]

    playlist_name = sp.playlist(playlist_URI)
    results = sp.playlist_tracks(playlist_URI)

    tracks = results["items"]

    playlist_name = playlist_name["name"]

    if not os.path.exists("./music/" + playlist_name):
        os.mkdir("music/" + playlist_name)

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])
    records = []
    for track in tracks:
        track_name = track["track"]["name"]
        track_artist = track["track"]["artists"][0]["name"]
        track_album = track["track"]["album"]["name"]

        image_link = track["track"]["album"]["images"][0]["url"]
        title_final = track_name.replace("/", "")
        title_final = title_final.replace('"', "")
        title = title_final.replace(".", "")

        record = {
            "titolo": title,
            "artista": track_artist,
            "album": track_album,
            "image": image_link,
        }
        records.append(record)

    with open("records.json", "w") as file:
        json.dump(records, file, indent=4)
    file.close()
    return playlist_name
