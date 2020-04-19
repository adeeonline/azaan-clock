from datetime import datetime as dt
from adhan import adhan
import adhan.methods
import datetime, sys, random, time, pygame, os, os.path, calendar

class AzaanClock:

    def __init__(self, caculationMethod, asrMethod, coordinates):
        self.caculationMethod = caculationMethod
        self.asrMethod = asrMethod
        self.currentUtcOffset = -((calendar.timegm(time.gmtime()) - calendar.timegm(time.localtime()))) / 3600
        self.coordinates = (coordinates["lat"], coordinates["lng"])
        dirname = os.path.dirname(__file__)
        assetsDir = '../assets/audio/'
        self.basePath = os.path.join(dirname, assetsDir)
        

    def playAzaan(self, azaan):
        filePath = ""
        if azaan == "fajr":
            filePath = self.basePath + "fajr/" + self.getRandomFile(self.basePath + "fajr/")
        else:
            filePath = self.basePath + self.getRandomFile(self.basePath)

        self.playSoundAtPath(filePath)


    def getCurrentAzaan(self, adhanTimes):
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
    

    def getRandomFile(self, path):
        files = []
        for (_, _, filenames) in os.walk(path):
            files.extend(filenames)
            break
        fileCount = len(files) - 1
        random.seed(time.clock())
        index = random.randint(0, fileCount)
        return files[index]


    def playSoundAtPath(self, path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue


    def getAzaanNameAndTime(self, date):
        offset = self.currentUtcOffset
        methodsMap = {
            "isna": adhan.methods.ISNA,
            "muslim-world-league": adhan.methods.MUSLIM_WORLD_LEAGUE,
            "egypt": adhan.methods.EGYPT,
            "makkah": adhan.methods.MAKKAH,
            "karachi": adhan.methods.KARACHI,
            "tehran": adhan.methods.TEHRAN,
            "shia": adhan.methods.SHIA
        }
        asrMethodMap = {
            "hanafi": adhan.methods.ASR_HANAFI,
            "standard": adhan.methods.ASR_STANDARD
        }

        params = {}
        params.update(methodsMap[self.caculationMethod])
        params.update(asrMethodMap[self.asrMethod])
        azaanDate = date

        adhanTimes = adhan.adhan(
            day=azaanDate,
            location=self.coordinates,
            parameters=params,
            timezone_offset=offset,
        )
        
        del adhanTimes["shuruq"]
        return self.getCurrentAzaan(adhanTimes)

    
    def getAzaanTimes(self, date):
        nameAndTime = self.getAzaanNameAndTime(date)
            
        if nameAndTime[0] == "":
            date = date + datetime.timedelta(days = 1)
            nameAndTime = self.getAzaanNameAndTime(date)
        
        return nameAndTime


    def start(self):
        while True:    
            date = dt.today()
            nameAndTime = self.getAzaanTimes(date)
            print(nameAndTime)
            time.sleep(nameAndTime[1])
            self.playAzaan(nameAndTime[0])



