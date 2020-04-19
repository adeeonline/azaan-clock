import sys, time, os, json, datetime
from datetime import datetime as dt
from src.AzaanClock import AzaanClock

TIME_TO_RESTART_BLUETOOTH = 120

def bluetoothConnected():
    status = os.system('ls /dev/input/ | grep event0 > /dev/null')
    print(status)
    if status == 0:
        return True 
    else:
        return False


with open(os.path.dirname(__file__) + '../config.json') as jsonFile:
    configs = json.load(jsonFile)

azaanClock = AzaanClock(
    configs["calculation-method"], 
    configs["asr-method"],
    configs["coordinates"]
)

while True:
    date = dt.today()
    nameAndTime = azaanClock.getAzaanTimes(date)
    sleepTime = nameAndTime[1] - TIME_TO_RESTART_BLUETOOTH
    
    print('Current Time: ' + dt.now())
    print('Sleeping For: ' + sleepTime)

    time.sleep(sleepTime)
    
    print('Restarting Bluetooth service before Azaan')
    os.system('sudo systemctl restart bluetooth.service')