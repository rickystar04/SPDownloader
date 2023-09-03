import os

import moviepy.editor as mp
from tqdm import tqdm


def extract_audio(video_path, playlist_name, savename):
    # with tqdm(total=100, desc="Sending", unit="B", unit_scale=True) as pbar:
    clip = mp.VideoFileClip(video_path, verbose=False)
    clip.audio.write_audiofile("music/" + playlist_name + "/" + savename, logger=None)
    clip.close()
    os.remove(video_path)
