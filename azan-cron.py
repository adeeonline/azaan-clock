from datetime import datetime, time
from adhan import adhan
from adhan.methods import ISNA, ASR_HANAFI
import pygame

city_coordinates = (37.3441254,-121.9806518)
timezone_offset = -8
params = {}
params.update(ISNA)
params.update(ASR_HANAFI)

adhan_times = adhan(
    day=datetime.today(),
    location=city_coordinates,
    parameters=params,
    timezone_offset=timezone_offset,
)

del adhan_times["shuruq"]
print (adhan_times)
print (datetime.now())

pygame.mixer.init()
pygame.mixer.music.load('./assets/audio/azan.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
