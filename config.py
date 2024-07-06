import eel
import sys
import threading
from queue import Queue

HOST = '0.0.0.0'
PORT = 7075
CHANNELS = 32

drum_sounds = {
    'drum1': 'drum_sounds/drum1.wav',
    'drum2': 'drum_sounds/drum2.wav',
    'drum3': 'drum_sounds/drum3.wav',
    'drum4': 'drum_sounds/drum4.wav',
    'drum5': 'drum_sounds/drum5.wav',
    'drum6': 'drum_sounds/drum6.wav',
    'drum7': 'drum_sounds/drum7.wav',
    'drum8': 'drum_sounds/drum8.wav',
    'drum9': 'drum_sounds/drum9.wav',
}

server_running = False
stop_event = threading.Event()
command_queue = Queue()  #eel commands

def init_eel():
    try:
        eel.init('web')
    except Exception as e:
        print(f"Failed to initialize Eel: {e}")
        sys.exit(1)