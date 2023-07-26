from spotipy.oauth2 import SpotifyOauthError

from . import cred


def check_secrets():
    if cred.CLIENT_ID is None and cred.CLIENT_SECRET is None:
        raise SpotifyOauthError("Client ID and Client Secret not present")

    elif cred.CLIENT_ID is None:
        raise SpotifyOauthError("Client ID not present")

    elif cred.CLIENT_SECRET is None:
        raise SpotifyOauthError("Client Secret not present")
