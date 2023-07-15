# Welcome to SPDownloader 👋

> SPDownloader is a tool for downloading all the tracks contained in a Spotify playlist in MP3 format

## Requirements

- [Python](https://www.python.org/) 3.8+ and Pip

- [FFmpeg](https://www.ffmpeg.org/)

- [Spotify](https://spotify.com) account

[Click Here](https://youtu.be/EyIIvctDhYc) if you are on Windows and don't know how to install [FFmpeg](https://www.ffmpeg.org/)

## Installation

```bash
git clone https://github.com/rickystar04/SPDownload.git
cd SPDownload
cp .env.example .env
pip install -r requirements.txt
```

open the `.env` file and fill it in with asked values.

To get `client_ID` and `client_SECRET` you need to:

1. Connect to <https://developer.spotify.com/dashboard> and login.
1. Accept the terms of service (if this is your first time logging in).
1. Select `Create an App` and enter any name you want but in the `Redirect URI` enter `http://localhost:9000`
1. now copy `Client Id` and `Client Secret` and paste it in the `.env` file present in root folder

## Usage

On spotify, open the playlist you want to download, click the 3 dots and share>copy link to playlist

![image](https://img001.prntscr.com/file/img001/zpVhvud8SqSqvOsu5m-7Tg.png)

```python
python3 spdownloader.py
```

OR if you are on `Windows`

```python
py spdownloader.py
```

## Disclaimer

Please note that the following method should not be considered a replacement for purchasing Spotify Premium. Its purpose is solely educational. It should be noted that this method retrieves songs from YouTube, which is why the downloaded songs may not always match the original tracks available on Spotify. Hence another reason why this is not a substitute of Spotify Premium

## 🤝 Contributing

Contributions, issues and feature requests are welcome!

## Author

- Github: [rickystar04](https://github.com/rickystar04)
- Email: [rickybenincasa04@gmail.com](mailto:rickybenincasa04@gmail.com)
