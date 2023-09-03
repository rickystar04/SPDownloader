import eyed3
import json
import os
import urllib.request


def image(playlist_name, type):
    with open("records.json") as file:
        records = json.load(file)

    for record in records:
        title = record["titolo"]
        path = "music/" + playlist_name + "/" + title + ".mp3"
        try:
            audio = eyed3.load(path)
        except FileNotFoundError:
            print("File not found.")
            exit()
        except Exception as e:
            print(f"Error loading the file: {str(e)}")
            exit()
        with open("images/" + title + " cover", "rb") as cover:
            audio.tag.images.set(3, cover.read(), "image/jpeg")

        tag = audio.tag

        if type == "playlist":
            tag.artist = record["artista"]
            tag.album = record["album"]["name"]

        elif type == "album":
            tag.artist = record["artista"]
            tag.album = record["album"]

        audio.tag.save()


def image2(record, playlist):
    title = record["titolo"]
    path = "music/" + playlist + "/" + title + ".mp3"
    try:
        audio = eyed3.load(path)
    except FileNotFoundError:
        print("File not found.")
        exit()
    except Exception as e:
        print(f"Error loading the file: {str(e)}")
        exit()

    img = open(os.path.join("images", title + " cover"), "wb")
    img.write(urllib.request.urlopen(record["image"]).read())
    img.close()
    with open("images/" + title + " cover", "rb") as cover:
        audio.tag.images.set(3, cover.read(), "image/jpeg")

    tag = audio.tag
    print("prova")
    if type == "playlist":
        tag.artist = record["artista"]
        tag.album = record["album"]["name"]

    elif type == "album":
        tag.artist = record["artista"]
        tag.album = record["album"]
    audio.tag.save()
