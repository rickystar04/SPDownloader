# SPDownloader

SPDownloader is a Python-based tool that allows you to download all the tracks from a Spotify playlist or album in MP3 format.

## Prerequisites

- Python and pip installed and updated on your system.

## Getting Started

1. Visit the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in.
2. Accept the terms of service (if this is your first time logging in).
3. Select "Create an App" and enter any name you want.
4. Copy the Client Id and Client Secret.

## Setup

1. Clone this repository to your local machine.
2. Run `setup.py` to install the necessary dependencies.
3. Run the "spdownloader.py" file once to create the .env file, then edit it by entering the client_id and client_secret you copied previously
4. Paste the Client Id and Client Secret into the appropriate fields in the newly created `.env` file

## Usage

1. Open Spotify and navigate to the playlist or album you want to download.
2. Click the 3 dots and select share > copy link to playlist.
3. Run `python3 spdownloader.py` in your terminal.
4. Paste the link to the playlist or album

## Contributing

We welcome any improvements, advice, or suggestions. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the GNU General Public License v3.0. See the `LICENSE` file for more details.

## Contact

For any queries, you can reach out to the maintainer at rickybenincasa04@gmail.com.
