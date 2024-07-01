import os
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()


    os.system('start msedge.exe --app="http://indexx.html"')

    eel.start('indexx.html', mode=None, block=True)
