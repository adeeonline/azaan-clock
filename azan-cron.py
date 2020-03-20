from datetime import datetime
from adhan import adhan
from adhan.methods import ISNA, ASR_HANAFI
import sys, random, time, pygame, os, os.path

def playAzaan(azaan):
    filePath = './assets/audio/fajr/azan-fajr.mp3'
    
    if azaan != "fajr":
        files = next(os.walk("./assets/audio/"))
        file_count = len(files[2]) - 1
        number = str(random.randint(1, file_count))
        filePath = './assets/audio/azan-' + number + '.mp3'

    pygame.mixer.init()
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue

def getAzaanNameAndTime():
    coordinates = (37.3441254,-121.9806518)
    offset = -7
    params = {}
    params.update(ISNA)
    params.update(ASR_HANAFI)

    adhanTimes = adhan(
        day=datetime.today(),
        location=coordinates,
        parameters=params,
        timezone_offset=offset,
    )
    del adhanTimes["shuruq"]

    azaanName = ""
    azaanSleepInterval = 86400

    for key in adhanTimes:
        d = adhanTimes[key] - datetime.now() 
        nextAzaanTime = int(d.total_seconds())
    
        if nextAzaanTime < azaanSleepInterval and nextAzaanTime > 0:
            azaanSleepInterval = nextAzaanTime
            azaanName = key

    return (azaanName, azaanSleepInterval)

while True:
    nameAndTime = getAzaanNameAndTime()
    print(nameAndTime)
    time.sleep(nameAndTime[1])
    playAzaan(nameAndTime[0])
