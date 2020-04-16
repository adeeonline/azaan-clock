import json, os
from src.AzaanClock import AzaanClock

with open(os.path.dirname(__file__) + '/config.json') as jsonFile:
    configs = json.load(jsonFile)

azaanClock = AzaanClock(
    configs["calculation-method"], 
    configs["asr-method"],
    configs["coordinates"]
)

azaanClock.start()
