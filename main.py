import os
import eel

from engine.features import *
from engine.command import *

def start():
    
    eel.init("www")

    playAssistantSound()


    os.system('start msedge.exe --app="http://localhost:8000/indexx.html"')

    eel.start('indexx.html', mode=None, host='localhost', block=True)
