import sys, time, os

while True:
    time.sleep(300)
    status = os.system('ls /dev/input/ | grep event0 > /dev/null')    
    print(status)
    if status != 0:
        print('Bluetooth is not connected so restarting the service')
        os.system('reboot')
        print('Done service restarting')