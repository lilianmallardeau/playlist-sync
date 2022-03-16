#!/usr/bin/env python3
import os
import sys
import json
import click

from .config import Config
from .deemix_config import DeemixConfig
from .playlist import Playlist

CONFIG_FILE = "config.json"
PLAYLIST_FILE = "playlists.json"

DEFAULT_PLAYLISTS = [
    {
        "url": "https://deezer.com/playlist/12345678...",
        "folder": "PLAYLIST_FOLDER",
        "overwrite": False
    },
    {
        "url": "https://open.spotify.com/playlist/abcd1234...",
        "folder": "PLAYLIST_FOLDER",
        "overwrite": False
    }
]


@click.group()
def cli():
    pass

@cli.command()
def init():
    config = Config(CONFIG_FILE, initialize=True)
    if (not config.exists()) or input(f"{config.config_file} already exists. Overwrite? (y/N) ").lower() == 'y':
        config.save()
    if (not os.path.isfile(PLAYLIST_FILE)) or input(f"{PLAYLIST_FILE} already exists. Overwrite? (y/N) ").lower() == 'y':
        with open(PLAYLIST_FILE, "w") as playlist_file:
            json.dump(DEFAULT_PLAYLISTS, playlist_file, indent=4)

@cli.command()
def sync():
    if not (os.path.isfile(CONFIG_FILE) and os.path.isfile(PLAYLIST_FILE)):
        print(f"{CONFIG_FILE} or {PLAYLIST_FILE} doesn't exist. Run `{sys.argv[0]} init` to initialize.")
        return
    
    # Reading config
    config = Config(CONFIG_FILE)
    deemix_config = DeemixConfig("config", arl=config['arl'])
    deemix_config.setSpotifyConfig(config['spotifyClientId'], config['spotifyClientSecret'])
    deemix_config.setDefaultBitrate(config['defaultBitrate'], fallback=bool(config['fallbackBitrate']))
    deemix_config.setOverwrite(bool(config['overwriteFiles']))
    deemix_config['saveArtwork'] = config['saveArtwork']

    # Reading playlists file and syncing each playlist
    for playlist in json.load(open(PLAYLIST_FILE)):
        playlist_obj = Playlist(playlist['url'], playlist['folder'], deemix_config)
        playlist_obj.sync(overwrite_files=bool(playlist['overwrite']) if 'overwrite' in playlist else False)
    
    deemix_config.clear()


if __name__ == '__main__':
    cli()
