import moviepy.editor as mp
import os

def extract_audio(video_path, playlist_name, savename):
	clip=mp.VideoFileClip(video_path)
	clip.audio.write_audiofile("music/"+playlist_name+"/"+savename)
	os.remove(video_path)
	print("Done")


def path(video_path, playlist_name, savename):
	extract_audio(video_path, playlist_name, savename)

