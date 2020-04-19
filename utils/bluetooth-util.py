import sys, time, os, json, datetime
from datetime import datetime as dt
PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from src.AzaanClock import AzaanClock

TIME_TO_RESTART_BLUETOOTH = 120

def bluetoothConnected():
    status = os.system('ls /dev/input/ | grep event0 > /dev/null')
    print(status)
    if status == 0:
        return True 
    else:
        return False

relPath = os.path.dirname(__file__)
if (relPath != ""):
    relPath = relPath + "/"

with open(relPath + '/../config.json') as jsonFile:
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
    
    print('Current Time: ' + dt.now().__str__())
    print('Sleeping For: ' + sleepTime.__str__())

    time.sleep(sleepTime)
    
    print('Restarting Bluetooth service before Azaan')
    os.system('sudo systemctl restart bluetooth.service')