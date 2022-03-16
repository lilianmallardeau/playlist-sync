import os
import shutil
from pathlib import Path
import json

DEFAULT_CONFIG = {
  "downloadLocation": os.getcwd(),
  "tracknameTemplate": "%artist% - %title%",
  "albumTracknameTemplate": "%tracknumber% - %title%",
  "playlistTracknameTemplate": "%position% - %artist% - %title%",
  "createPlaylistFolder": True,
  "playlistNameTemplate": "%playlist%",
  "createArtistFolder": False,
  "artistNameTemplate": "%artist%",
  "createAlbumFolder": True,
  "albumNameTemplate": "%artist% - %album%",
  "createCDFolder": True,
  "createStructurePlaylist": False,
  "createSingleFolder": False,
  "padTracks": True,
  "paddingSize": "0",
  "illegalCharacterReplacer": "_",
  "queueConcurrency": 3,
  "maxBitrate": "3",
  "feelingLucky": False,
  "fallbackBitrate": True,
  "fallbackSearch": False,
  "fallbackISRC": False,
  "logErrors": True,
  "logSearched": False,
  "overwriteFile": "n",
  "createM3U8File": False,
  "playlistFilenameTemplate": "playlist",
  "syncedLyrics": False,
  "embeddedArtworkSize": 800,
  "embeddedArtworkPNG": False,
  "localArtworkSize": 1400,
  "localArtworkFormat": "jpg",
  "saveArtwork": True,
  "coverImageTemplate": "cover",
  "saveArtworkArtist": False,
  "artistImageTemplate": "folder",
  "jpegImageQuality": 90,
  "dateFormat": "Y-M-D",
  "albumVariousArtists": True,
  "removeAlbumVersion": False,
  "removeDuplicateArtists": True,
  "featuredToTitle": "0",
  "titleCasing": "nothing",
  "artistCasing": "nothing",
  "executeCommand": "",
  "tags": {
    "title": True,
    "artist": True,
    "artists": True,
    "album": True,
    "cover": True,
    "trackNumber": True,
    "trackTotal": False,
    "discNumber": True,
    "discTotal": False,
    "albumArtist": True,
    "genre": True,
    "year": True,
    "date": True,
    "explicit": False,
    "isrc": True,
    "length": True,
    "barcode": True,
    "bpm": True,
    "replayGain": False,
    "label": True,
    "lyrics": False,
    "syncedLyrics": False,
    "copyright": False,
    "composer": False,
    "involvedPeople": False,
    "source": False,
    "rating": False,
    "savePlaylistAsCompilation": False,
    "useNullSeparator": False,
    "saveID3v1": True,
    "multiArtistSeparator": "default",
    "singleAlbumArtist": False,
    "coverDescriptionUTF8": False
  }
}
DEFAULT_SPOTIFY_CONFIG = {
  "clientId": "",
  "clientSecret": "",
  "fallbackSearch": False
}

class DeemixConfig():
    def __init__(self, config_folder: str = "config", arl: str = None, overwrite: bool = True) -> None:
        self.config_folder = Path(config_folder)
        if arl:
            self.arl = arl
        self._config = DEFAULT_CONFIG
        self._spotify_config = DEFAULT_SPOTIFY_CONFIG
        if not overwrite:
            self.load()

    def save(self):
        os.makedirs(self.config_folder / "spotify", exist_ok=True)
        
        with open(self.config_folder / "config.json", "w") as config_file:
            json.dump(self._config, config_file, indent=4)
        with open(self.config_folder / "spotify" / "config.json", "w") as config_file:
            json.dump(self._spotify_config, config_file, indent=4)
        with open(self.config_folder / ".arl", "w") as arl_file:
            arl_file.write(self.arl)
    
    def clear(self):
        shutil.rmtree(self.config_folder)

    def load(self):
        # TODO
        raise NotImplementedError()

    def setSpotifyConfig(self, client_id, secret, fallbackSearch=None):
        self._spotify_config["clientId"] = str(client_id)
        self._spotify_config["clientSecret"] = str(secret)
        if fallbackSearch is not None:
            self._spotify_config["fallbackSearch"] = bool(fallbackSearch)
    
    def setDefaultBitrate(self, bitrate, fallback=None):
        if bitrate == 128:
            self._config['maxBitrate'] = 1
        elif bitrate == 320:
            self._config['maxBitrate'] = 3
        elif bitrate == 'flac':
            self._config['maxBitrate'] = 9
        else:
            raise ValueError(f"`bitrate` must be either 128, 320 or 'flac', got {bitrate}")
        
        if fallback is not None:
            self._config['fallbackBitrate'] = bool(fallback)
    
    def setOverwrite(self, overwrite: bool):
        self._config['overwriteFile'] = 'y' if overwrite else 'n'
    
    def __getitem__(self, key):
        return self._config[key]

    def __setitem__(self, key, value):
        self._config[key] = value
