import pystray
from PIL import Image
from pystray import MenuItem as item
import win32api
import time
import os
import sys
import ctypes

whnd = ctypes.windll.kernel32.GetConsoleWindow()
if whnd != 0:
    ctypes.windll.user32.ShowWindow(whnd, 0)
    ctypes.windll.kernel32.CloseHandle(whnd)

icon = pystray.Icon('SAVER')
"""bigblack.ico is the icon of the system tray"""
image = Image.open('bigblack.ico')
icon.icon = image

def setup(icon):
    """Display the tray icon"""
    icon.visible = True

def Start():
    """right click -- entry the main program"""
    # First step-- <Saviour -- system stray>
    import Saviour
    Saviour.Saviour()

    # Second step--<search -- system stray>
    if Saviour.sign_1 == True:
        import search
        search.search()

    # Third step--<compress -- system stray>
    if search.sign_2 == True:
        import compress
        compress.compress()

    # Fourth step--<launch -- system stray>
    if compress.sign_3 == True:
        import launch_check
        if launch_check.sign_4 == True:
            import launch_final

    # Fifth step-- <boom -- system stray>
    if launch_check.sign_4 == True:
        import boom
        win32api.PostQuitMessage(0)
        sys.exit()
        

def Exit():
    """right click -- exit from the menu"""
    time.sleep(0.5)
    win32api.PostQuitMessage(0)
    sys.exit()

    """settings of the menu"""
menu = (item('Start', Start),
        item('Exit', Exit))
icon = pystray.Icon("name", image, "SAVER", menu)
icon.run(setup)
