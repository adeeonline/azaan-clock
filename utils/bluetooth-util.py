import sys, time, os, subprocess

while True:
    status = subprocess.call('ls /dev/input/event0 2>/dev/null', shell=True)
    if status == False:
        print('Bluetooth is not connected so restarting the service')
        subprocess.call('systemctl restart bluetooth.service')
        print('Done restarting service')
    
    time.sleep(5)