import os
import re
import sys
import time
import json
import threading
import urllib.error
from tqdm import tqdm
import urllib.request
from modules.color import *
from modules.metadata import *
import yt_dlp


yt_opts = {
    "verbose": False,
    "download_sections": [{"section": {"start_time": 2, "end_time": 7}}],
}

ydl = yt_dlp.YoutubeDL()


# Creiamo il Semaphore con un limite di 10 threads contemporanei
semaphore = threading.Semaphore(20)


def download_songs(record, filelocation, i, playlist, progress_callback):
    url = record["song_link"]
    # tqdm.write(f"Downloading song {i}...")
    try:
        html = urllib.request.urlopen(url)
        link = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        if len(link) > 0:
            url = "https://www.youtube.com/watch?v=" + link[0]
            # yt = YouTube(url)# , use_oauth=True, allow_oauth_cache=False)
            # video = yt.streams.first()

            # original = video.default_filename
            # video.download(filelocation)
            ydl_opts = {
                "noprogress": True,
                "quiet": True,
                "no_warnings": True,
                "format": "mp3/bestaudio/best",
                "outtmpl": filelocation + "/" + record["titolo"] + ".%(ext)s",
                "postprocessors": [
                    {  # Extract audio using ffmpeg
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                    }
                ],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                error_code = ydl.download(url)
                print(error_code)

            """
            os.rename(
                os.path.join("music", playlist, original),
                os.path.join("music", playlist, record["titolo"]),
            )

            extract_audio(
                os.path.join("music", playlist, record["titolo"]),
                playlist,
                record["titolo"] + ".mp3",
            )
            """
            tqdm.write(
                color.GREEN + record["titolo"] + " downloaded successfully!" + color.END
            )
        else:
            print(color.RED + "Can't retrieve any videoclip from this link" + color.END)

    except urllib.error.URLError as e:
        print("Error occurred during download of song " + record["titolo"])
        print("Error: Connection failed")

    except Exception as e:
        print("Error occurred during download of song " + record["titolo"])
        print("Error: " + str(e))

    try:
        img = open(os.path.join("images/", record["titolo"] + " cover.png"), "wb")
        img.write(urllib.request.urlopen(record["image"]).read())
        img.close()
        

    except urllib.error.URLError as e:
        print("Error occurred during download of image for " + record["titolo"])
        print("Error: Connection failed")

    semaphore.release()

    progress_callback()


def check(playlist, record, i, progress_callback):
    tqdm.write(color.GREEN + record["titolo"] + " already downloaded!" + color.END)
    tqdm.write("Verifying metadata...")
    image2(record, playlist)


def createNewDownloadThread(link, filelocation, i):
    download_thread = threading.Thread(
        target=download_songs, args=(link, filelocation, i)
    )
    download_thread.start()


def thread(playlist, song_len):
    global i
    s = time.perf_counter()
    i = 0
    progress_lock = threading.Lock()

    with open("records.json") as file:
        records = json.load(file)

    threads = []
    format = "Loading: {desc}{percentage:3.0f}%|{bar:100}"

    def update_progress():
        # global i
        i = 0
        # print("I:"+str(i))
        # with progress_lock:

        if i == len(records) - 1:
            tqdm.write("I:" + str(i))

        i += 1
        progress = (i / len(records)) * 100
        pbar.update(progress)
        sys.stdout.write("\x1b[2K")

    prova = "{desc}{percentage:3.0f}%|{bar:100}"
    with tqdm(
        total=100,
        desc="Downloading:",
        ascii="_#",
        file=sys.stdout,
        position=1,
        bar_format=prova,
    ) as pbar:
        time.sleep(1)
        for record in records:
            path = os.path.join("music", playlist)

            exist = os.path.exists(os.path.join(path, record["titolo"] + ".mp3"))

            if exist:
                # time.sleep(0.1)
                tqdm.write(
                    color.GREEN + record["titolo"] + " already downloaded!" + color.END
                )

                t = threading.Thread(
                    target=check,
                    args=(playlist, record, i, update_progress),
                )
            else:
                t = threading.Thread(
                    target=download_songs,
                    args=(record, path, i, playlist, update_progress),
                )
            threads.append(t)

            # Acquire the Semaphore before starting the thread
            semaphore.acquire()

            t.start()
            i += 1
        for t in threads:
            t.join()

            # Release the Semaphore after the thread has finished its work

    elapsed = time.perf_counter() - s
    print(f"\n\n{__file__} executed in {elapsed:0.2f} seconds.")
