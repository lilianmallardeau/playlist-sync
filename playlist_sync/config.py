import os
from pathlib import Path
import json

DEFAULT_CONFIG = {
    "arl": "YOUR_DEEZER_ARL",
    "spotifyClientId": "",
    "spotifyClientSecret": "",
    "defaultBitrate": 320,
    "fallbackBitrate": True,
    "overwriteFiles": False,
    "saveArtwork": True
}


class Config():
    def __init__(self, config_file, initialize=False) -> None:
        self.config_file = config_file
        if initialize:
            self._config = DEFAULT_CONFIG
        else:
            self.load()
    
    def save(self):
        json.dump(self._config, open(self.config_file, "w"), indent=4)
    
    def load(self):
        self._config = json.load(open(self.config_file))
    
    def exists(self):
        return os.path.isfile(self.config_file)
    
    def __getitem__(self, key):
        return self._config[key]

    def __setitem__(self, key, value):
        self._config[key] = value
