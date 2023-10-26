import os
import platform

# TODO
# aggiungere installazione ffmpeg per windows
if str(platform.system()) == "Windows":
    # qui installa ffmpeg
    print("Download")

else:
    os.system("sudo apt-get install ffmpeg")
os.system("pip install dotenv")
os.system("pip install urllib.request")
os.system("pip install spotipy")
os.system("pip install eyed3")
os.system("pip install pytube")
os.system("pip install ffmpeg")
os.system("pip install ffprobe")
os.system("pip install tqdm")
os.system("pip install pandas")
os.system("pip install requests")
os.system("pip install mutagen")
os.system("pip install flask")
os.system("pip install flask_session")
os.system("pip install yt-dlp")
