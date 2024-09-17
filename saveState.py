import json
from pathlib import Path
import os
def saveGameState():
    pass

assetsFolder = Path("assets")
if not assetsFolder.exists():
    os.mkdir(assetsFolder)
saveFile = Path("assets/saveFile.json")
saveStats = {
    "coins": 0,
    "employees": 0,
}
with saveFile.open("w") as f:
    json.dump(saveStats, f)