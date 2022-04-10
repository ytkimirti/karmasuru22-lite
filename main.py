from asyncio import subprocess
from sim.Sdk import cmd_debug
from sim.Sdk import cmd_ugv
from sim.Sdk import cmd_interop
from src import keyboard
from src import debug_keys
import time
import sys
import os
import subprocess

EXECUTABLE_FOLDER="sim"
EXECUTABLE_NAME="KARMASIM.exe"

# Exe doesn't work well when we are not cd'ed into it's directory
os.chdir(EXECUTABLE_FOLDER)
executable_path = os.path.abspath(EXECUTABLE_NAME)

print(f"Executing {executable_path}")
subprocess.Popen([executable_path])


while True:
    keyboard.perform_update()
    time.sleep(0.01)

    # Deneme
    debug_keys.print_state()
    debug_keys.update_keys()
