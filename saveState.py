import json
from pathlib import Path
import os

class SaveGame:

    def saveGameStateToFile(self):
        with self.save_file.open("w") as f:
            json.dump(self.save_stats, f)

    def loadGameStateFromFile(self):
        with self.save_file.open("r") as f:
            file_contents = f.read()
        file_contents = json.loads(file_contents)
        self.save_stats = file_contents

    def getGameState(self):
        return self.save_stats

    def setGameState(self, stats):
        self.save_stats = stats
        self.saveGameStateToFile()

    def __init__(self):
        self.assets_folder = Path("assets")
        self.save_file = Path("assets/saveFile.json")
        if not self.assets_folder.exists():
            os.mkdir(self.assets_folder)
        if not self.save_file.exists():
            self.save_stats = {
                "coins": 0,
                "employees": 0,
                "rating": 0,
                "buildings": [],
                "level": 0
            }
            self.saveGameStateToFile()
        self.loadGameStateFromFile()