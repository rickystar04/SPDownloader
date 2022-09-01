import eyed3

def image(path, artist, album, playlist_name):
	path=path
	a_file=eyed3.load("music/"+playlist_name+"/"+path+".mp3")
	
	with open("./images/"+path+" cover.jpg", "rb") as cover:
		a_file.tag.images.set(3, cover.read(),"image/jpg")

	a_file.tag.artist=artist
	a_file.tag.album=album
	a_file.tag.save()
