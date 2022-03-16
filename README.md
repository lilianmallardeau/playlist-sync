# Playlist-sync

`playlist-sync` is a little command line tool to download and sync playlists from Deezer or Spotify to predefined folders. It reads playlists links and target folders from a JSON file.

It uses [`deemix`](https://pypi.org/project/deemix/) under the hood to actually download the playlists.

## What you will need
- Python >= 3.8 with pip (untested on earlier versions of Python)
- A Deeezer account. Since `deemix` downloads songs from Deezer, it uses your Deezer account to access Deezer servers and download music. So even if you only want to download Spotify playlists, you will **need** to have a Deezer account. Note that to download 320kbps MP3 or FLAC, you will need a Deezer Premium account. A free Deezer account only allow to download 128kbps MP3.
- A Spotify account if you want to download playlists from Spotify.

## Installation
Playlist-sync can be installed with `pip` from [PyPI](https://pypi.org/project/playlist-sync/):
```
pip install playlist-sync
```
The pip package adds the `playlist-sync` command to the command line.

## How to setup and use
Playlist-sync relies on two files, `config.json` and `playlists.json`, which must exist in the current working directory. `config.json` contains some general settings (Deezer ARL, Spotify API token, bitrate...), and `playlists.json` contains the links to your playlists as well as the target folders where you want them to be downloaded.

`playlist-sync` can create templates for these two files so you only need to fill them. In your music library folder (where you want your playlists to be downloaded), run:
```
playlist-sync init
```

It will create the 2 json files. Fill them both as explained in the wiki, [here](https://github.com/lilianmallardeau/playlist-sync/wiki/The-config.json-file) and [here](https://github.com/lilianmallardeau/playlist-sync/wiki/The-playlists.json-file).
Once you've filled the `config.json` file with your Deezer ARL (and Spotify API client ID and secret if you want to download Spotify playlists) and the `playlists.json` file with your playlists links, to download them all at once in the desired folders, simply run:
```
playlist-sync sync
```


## How to install and use easily on Windows
1. If you don't have it installed already, download and install [Python](https://www.python.org). During installation, make sure to choose to update the PATH environment variable.
2. Open the command prompt (search for "cmd" in the search bar) and type `pip install playlist-sync`
3. Download the 2 scripts in the [`windows_scripts`](https://github.com/lilianmallardeau/playlist-sync/tree/main/windows_scripts) folder in this repo, and put them in your music library folder
4. Double click on `playlist-sync_init.cmd`. It will create two json files, `config.json` and `playlists.json`, in the same folder.
5. Fill the two json files as described [here](https://github.com/lilianmallardeau/playlist-sync/wiki/The-config.json-file) and [here](https://github.com/lilianmallardeau/playlist-sync/wiki/The-playlists.json-file).
6. To download/update your playlists, simply double click on the `playlist-sync_sync.cmd` file


---


## Todo
- Add support for SoundCloud and YouTube playlists, with [youtube-dl](http://ytdl-org.github.io/youtube-dl/)
- Sync Serato/rekordbox crates with downloaded playlists
- Use ISRC numbers to prevent downloading songs from different playlists twice, and make hardlinks between files instead
