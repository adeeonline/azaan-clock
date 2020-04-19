import json, os
from src.AzaanClock import AzaanClock

relPath = os.path.dirname(__file__)
if (relPath != ""):
    relPath = relPath + "/"

with open(relPath + 'config.json') as jsonFile:
    configs = json.load(jsonFile)

azaanClock = AzaanClock(
    configs["calculation-method"], 
    configs["asr-method"],
    configs["coordinates"]
)

azaanClock.start()
