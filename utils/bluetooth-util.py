import sys, time, os

def bluetoothConnected():
    status = os.system('ls /dev/input/ | grep event0 > /dev/null')
    print(status)
    if status == 0:
        return True 
    else:
        return False

while True:
    time.sleep(300)
    if bluetoothConnected() == False:
        print('Bluetooth is not connected so restarting the service')
        os.system('reboot')
        print('Done service restarting') 
        os.system('sudo systemctl restart bluetooth.service')
        time.sleep(120)
        os.system('sudo systemctl reboot')