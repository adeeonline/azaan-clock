from datetime import datetime as dt
from adhan import adhan
from adhan.methods import ISNA, ASR_HANAFI
import datetime, sys, random, time, pygame, os, os.path


def playAzaan(azaan):
    dirname = os.path.dirname(__file__)
    assetsDir = 'assets/audio/'
    basePath = os.path.join(dirname, assetsDir)
    filePath = basePath + 'fajr/azan-fajr.mp3'
    
    if azaan != "fajr":  
        files = next(os.walk(basePath))
        fileCount = len(files[2]) - 1
        number = str(random.randint(1, fileCount))
        filePath = basePath + 'azan-' + number + '.mp3'

    pygame.mixer.init()
    pygame.mixer.music.load(filePath)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


def getCurrentAzaan(adhanTimes):
    azaanName = ""
    azaanSleepInterval = 86400
    azaanTime = ""
    
    for key in adhanTimes:
        d = adhanTimes[key] - dt.now() 
        nextAzaanTime = int(d.total_seconds())
    
        if nextAzaanTime < azaanSleepInterval and nextAzaanTime > 0:
            azaanSleepInterval = nextAzaanTime
            azaanName = key
            azaanTime = adhanTimes[key]

    return (azaanName, azaanSleepInterval, azaanTime)


def getAzaanNameAndTime(date, coordinates):
    offset = -7
    params = {}
    params.update(ISNA)
    params.update(ASR_HANAFI)
    azaanDate = date

    adhanTimes = adhan(
        day=azaanDate,
        location=coordinates,
        parameters=params,
        timezone_offset=offset,
    )
    
    del adhanTimes["shuruq"]
    return getCurrentAzaan(adhanTimes)
    

coordinates = (37.3441254,-121.9806518)

while True:    
    date = dt.today()
    nameAndTime = getAzaanNameAndTime(date, coordinates)
    
    if nameAndTime[0] == "":
        date = date + datetime.timedelta(days = 1)
        nameAndTime = getAzaanNameAndTime(date, coordinates)
    
    print(nameAndTime)

    time.sleep(nameAndTime[1])
    playAzaan(nameAndTime[0])
