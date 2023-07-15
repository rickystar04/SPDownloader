import eyed3


def image(path_music, path_image, artist, album, playlist_name):
    a_file = eyed3.load(f"music/{playlist_name}/{path_music}.mp3")

    with open(f"./images/{path_image} cover.jpg", "rb") as cover:
        a_file.tag.images.set(3, cover.read(), "image/jpg")

    a_file.tag.artist = artist
    a_file.tag.album = album
    a_file.tag.save()
