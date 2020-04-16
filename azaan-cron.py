import json
from src.AzaanClock import AzaanClock

with open('config.json') as jsonFile:
    configs = json.load(jsonFile)

azaanClock = AzaanClock(
    configs["calculation-method"], 
    configs["asr-method"],
    configs["coordinates"]
)

azaanClock.start()