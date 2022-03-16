import os
from pathlib import Path

class Playlist():
    def __init__(self, url, folder, deemix_config):
        self.url = url
        self.folder = Path(folder)
        self._deemix_config = deemix_config
        
        self._deemix_config['downloadLocation'] = str(self.folder.absolute())
        self._deemix_config['createPlaylistFolder'] = False

    def sync(self, overwrite_files=False, suppress_output=False):
        self._deemix_config.setOverwrite(overwrite_files)
        self._deemix_config.save()
        return os.system(f"deemix --portable {self.url}{' > /dev/null' if suppress_output else ''}")
