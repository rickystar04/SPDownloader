import moviepy.editor as mp
import os

def extract_audio(video_path, playlist_name, savename):
	clip=mp.VideoFileClip(video_path, verbose=False)
	clip.audio.write_audiofile("music/"+playlist_name+"/"+savename, logger=None)
	clip.close()
	os.remove(video_path)
