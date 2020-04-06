# Azaan Clock

### Requirements

1. Python 2.7+
2. Raspberry Pi (or any computer which can run python)
3. Speakers (Hardwired or Bluetooth)

### Installation

1. Clone this repository
2. Run `pip install adhan`
3. Run `python azan-cron.py`

### Options

Azaan Times are calculated based on various options. Here are some ways on how to configure them:

**Geo location Coordinates**
You can change the current location coordinates by opening `azan-cron.py` file and change this line `coordinates = (37.3441254,-121.9806518)` to use your location coordinates.

*Default: `(37.3441254,-121.9806518)`*

**Azan Time Calculation Method**
Azan times are calculated based on some method there are various methods provided by the Adhan library I am using. You can change the caculation method by going to `azan-cron.py`

1. Import the method you want here `from adhan.methods import ISNA, ASR_HANAFI`
2. Update these line with yoru methods 
`params.update(ISNA)`
`params.update(ASR_HANAFI)`

For all available options please visit the original library page here https://github.com/hayalasalah/adhan.py

*Default: `ISNA` and `ASR_HANAFI`*

**Adding More Azan Sounds**
You can add more Azan sounds. Goto `assets/audio` and add more Azan but make sure the file is in this format `azan-<increment-number>` E.g: `azan-1.mp3`

*Default: `1 Fajr, 2 Regular`*


### Credits
I used this library https://github.com/hayalasalah/adhan.py for calculating azan times.


