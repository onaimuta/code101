# import os
# devices = []
# for device in os.popen('arp -a'): devices.append(device)

import kthread #pip install kthread
from time import sleep
import subprocess

def getips():
    ipadressen = {}
    def ping(ipadresse):
        try:
            outputcap = subprocess.run([f'ping', ipadresse, '-n', '1'], capture_output=True) #sends only one package, faster
            ipadressen[ipadresse] = outputcap
        except Exception as Fehler:
            print(Fehler)
    t = [kthread.KThread(target = ping, name = f"ipgetter{ipend}", args=(f'192.168.100.{ipend}',)) for ipend in range(255)] #prepares threads
    [kk.start() for kk in t] #starts 255 threads
    while len(ipadressen) < 255:
        print('Searching network')
        sleep(.3)
    alldevices = []
    for key, item in ipadressen.items():
        if not 'unreachable' in item.stdout.decode('utf-8') and 'failure' not in item.stdout.decode('utf-8'): #checks if there wasn't neither general failure nor 'unrechable host'
            alldevices.append(key)
    return alldevices

allips = getips() #takes 1.5 seconds on my pc