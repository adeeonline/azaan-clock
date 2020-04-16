# Azaan Clock

### Requirements

1. Python 2.7+
2. Raspberry Pi (or any computer which can run python)
3. Speakers (Hardwired or Bluetooth)

### Installation

1. Clone this repository
2. Run `pip install -r requirements.txt`
3. Open `config.json` and fill in details
4. Run `python azaan-cron.py`

### Configure config.json

Azaan Times are calculated based on various options which you can change in `config.json`. Here are some ways on how to configure them:

**coordinates**
You can change the `lat` and `lng` in `config.json`
*Default: `(37.3441254,-121.9806518)`*

**calculation-method**
- isna
- muslim-world-league
- egypt
- makkah
- karachi
- tehran
- shia

*Default: `isna`*

**asr-method**
- standard
- hanafi

*Default: `hanafi`*

### Adding More Azan Sounds
You can add more Azan sounds by copying azaan sound files to `assets/audio` directory for regular azaan or `assets/audio/fajr` for fajr azaan.

*Default: `1 Fajr, 2 Regular`*

### Credits
I used this library https://github.com/hayalasalah/adhan.py for calculating azan times.


