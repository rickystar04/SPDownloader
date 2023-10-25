import os
import platform

# TODO
# aggiungere installazione ffmpeg per windows
if str(platform.system()) == "Windows":
    # qui installa ffmpeg
    print("INSTALLA")

else:
    os.system("sudo apt-get install ffmpeg")
os.system("python -m pip install dotenv")
os.system("python -m pip install urllib.request")
os.system("python -m pip install spotipy")
os.system("python -m pip install eyed3")
os.system("python -m pip install pytube")
os.system("python -m pip install ffmpeg")
os.system("python -m pip install ffprobe")
os.system("python -m pip install tqdm")
os.system("python -m pip install pandas")
os.system("python -m pip install requests")
os.system("python -m pip install mutagen")
os.system("python -m pip install flask")
os.system("python -m pip install flask_session")
os.system("python -m pip install yt-dlp")
