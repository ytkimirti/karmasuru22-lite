from asyncio import subprocess
from sim.Sdk import cmd_debug
from sim.Sdk import cmd_ugv
from sim.Sdk import cmd_interop
from src import keyboard
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

_crashes_enabled = True
_limits_enabled = True
_show_nodes = False
_show_limits = False
_infinite_supply = False
_controlling_ugv = 1
_fire_hose_dir = [0, 0, 1]
_fire_hose_pressure = 0
_subject_station = 1


def print_state():
    print("\r", end="")
    # print("[F2]Kazalar:" + ("1" if _crashes_enabled else "0"), end=" ")
    # print("[F3]Limitler:" + ("1" if _limits_enabled else "0"), end=" ")
    print("[F6-F7]IKA-ID:" + str(_controlling_ugv), end=" ")
    # print("[F8]SınırsızKaynak:" + ("1" if _infinite_supply else "0"), end=" ")
    print("[zxcvbn]SuYonu:" + str(_fire_hose_dir), end=" ")
    print("[ad]SuBasinci:" + str(_fire_hose_pressure), end=" ")
    print("[F11-F12]IkmalNokt-ID:" + str(_subject_station), end=" ")
    print("", end="", flush=True)

# Key names for reference
#['__class__', '__doc__', '__members__', '__module__', 'alt', 'alt_l', 'alt_r', 
#  'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete', 
#  'down', 'end', 'enter', 'esc', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 
#  'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
#  'home', 'insert', 'left', 'media_next', 'media_play_pause', 'media_previous', 
#  'media_volume_down', 'media_volume_mute', 'media_volume_up', 'menu', 'num_lock', 
#  'page_down', 'page_up', 'pause', 'print_screen', 'right', 'scroll_lock', 'shift', 
#  'shift_r', 'space', 'tab', 'up']

while True:
    keyboard.perform_update()
    print_state()
    time.sleep(0.01)

    if keyboard.get_key_down('f2'):
        _crashes_enabled = not _crashes_enabled
        cmd_debug.crash_enabled(_crashes_enabled)
    if keyboard.get_key_down('f3'):
        _limits_enabled = not _limits_enabled
        cmd_debug.limits_enabled(_limits_enabled)
    if keyboard.get_key_down('f4'):
        _show_nodes = not _show_nodes
        cmd_debug.show_nodes(_show_nodes)
    if keyboard.get_key_down('f5'):
        _show_limits = not _show_limits
        cmd_debug.show_limits(_show_limits)
    if keyboard.get_key_down('f8'):
        _infinite_supply = not _infinite_supply
        cmd_debug.infinite_supply(_infinite_supply)
    if keyboard.get_key_down('f6'):
        _controlling_ugv -= 1
        if _controlling_ugv < 1:
            _controlling_ugv = 1
    if keyboard.get_key_down('f7'):
        _controlling_ugv += 1
    if keyboard.get_key_down('e'):
        cmd_ugv.start_motor(_controlling_ugv)
    if keyboard.get_key_down('q'):
        cmd_ugv.stop_motor(_controlling_ugv)
    if keyboard.get_key_down('+'):
        cmd_ugv.set_gear(_controlling_ugv, True)
    if keyboard.get_key_down('-'):
        cmd_ugv.set_gear(_controlling_ugv, False)
    if keyboard.get_key_down('o'):
        cmd_ugv.set_handbrake(_controlling_ugv, True)
    if keyboard.get_key_down('l'):
        cmd_ugv.set_handbrake(_controlling_ugv, False)
    if keyboard.get_key_down('0'):
        cmd_ugv.set_turn_choice(_controlling_ugv, 0)
    if keyboard.get_key_down('1'):
        cmd_ugv.set_turn_choice(_controlling_ugv, 1)
    if keyboard.get_key_down('t'):
        cmd_ugv.start_supply(_controlling_ugv, _subject_station, cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('g'):
        cmd_ugv.start_supply(_controlling_ugv, _subject_station, cmd_interop.SUPPLY_WATER)
    if keyboard.get_key_down('y'):
        cmd_ugv.stop_supply(_controlling_ugv, cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('h'):
        cmd_ugv.stop_supply(_controlling_ugv, cmd_interop.SUPPLY_WATER)
    if keyboard.get_key_down('d'):
        _fire_hose_pressure += 0.1
        cmd_ugv.adjust_firehose(_controlling_ugv, _fire_hose_pressure)
    if keyboard.get_key_down('a'):
        _fire_hose_pressure -= 0.1
        if _fire_hose_pressure < 0:
            _fire_hose_pressure = 0
        cmd_ugv.adjust_firehose(_controlling_ugv, _fire_hose_pressure)
    if keyboard.get_key_down('z'):
        _fire_hose_dir[0] -= 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('x'):
        _fire_hose_dir[0] += 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('c'):
        _fire_hose_dir[1] -= 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('v'):
        _fire_hose_dir[1] += 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('b'):
        _fire_hose_dir[2] -= 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('n'):
        _fire_hose_dir[2] += 1
        cmd_ugv.align_firehose(_controlling_ugv, _fire_hose_dir[0], _fire_hose_dir[1], _fire_hose_dir[2])
    if keyboard.get_key_down('f11'):
        _subject_station -= 1
        if _subject_station < 1:
            _subject_station = 1
    if keyboard.get_key_down('f12'):
        _subject_station += 1

    cmd_ugv.set_throttle(_controlling_ugv, 1 if keyboard.get_key('w') else 0)
    cmd_ugv.set_brake(_controlling_ugv, 1 if keyboard.get_key('s') else 0)
