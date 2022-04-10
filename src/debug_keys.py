from . import keyboard
from ..sim.Sdk import cmd_ugv
from ..sim.Sdk import cmd_debug
from ..sim.Sdk import cmd_interop

class DebugState:
    _crashes_enabled = True
    _limits_enabled = True
    _show_nodes = False
    _show_limits = False
    _infinite_supply = False
    _controlling_ugv = 1
    _fire_hose_dir = [0, 0, 1]
    _fire_hose_pressure = 0
    _subject_station = 1

state = DebugState()

def print_state():
    print("\r", end="")
    # print("[F2]Kazalar:" + ("1" if _crashes_enabled else "0"), end=" ")
    # print("[F3]Limitler:" + ("1" if _limits_enabled else "0"), end=" ")
    print("[F6-F7]IKA-ID:" + str(state._controlling_ugv), end=" ")
    # print("[F8]SınırsızKaynak:" + ("1" if _infinite_supply else "0"), end=" ")
    print("[zxcvbn]SuYonu:" + str(state._fire_hose_dir), end=" ")
    print("[ad]SuBasinci:" + str(state._fire_hose_pressure), end=" ")
    print("[F11-F12]IkmalNokt-ID:" + str(state._subject_station), end=" ")
    print("", end="", flush=True)

# Key names for reference
#  'backspace', 'caps_lock', 'cmd', 'cmd_r', 'ctrl', 'ctrl_l', 'ctrl_r', 'delete', 
#  'down', 'end', 'enter', 'esc', 'f1'
#  'home', 'insert', 'left', 'media_next', 'media_play_pause', 'media_previous', 
#  'media_volume_down', 'media_volume_mute', 'media_volume_up', 'menu', 'num_lock', 
#  'page_down', 'page_up', 'pause', 'print_screen', 'right', 'scroll_lock', 'shift', 
#  'shift_r', 'space', 'tab', 'up']

def update_firehose():
    global state
    cmd_ugv.align_firehose(state._controlling_ugv, state._fire_hose_dir[0], state._fire_hose_dir[1], state._fire_hose_dir[2])


def update_keys():
    global state
    if keyboard.get_key_down('f2'):
        state._crashes_enabled = not state._crashes_enabled
        cmd_debug.crash_enabled(state._crashes_enabled)
    if keyboard.get_key_down('f3'):
        state._limits_enabled = not state._limits_enabled
        cmd_debug.limits_enabled(state._limits_enabled)
    if keyboard.get_key_down('f4'):
        state._show_nodes = not state._show_nodes
        cmd_debug.show_nodes(state._show_nodes)
    if keyboard.get_key_down('f5'):
        state._show_limits = not state._show_limits
        cmd_debug.show_limits(state._show_limits)
    if keyboard.get_key_down('f8'):
        state._infinite_supply = not state._infinite_supply
        cmd_debug.infinite_supply(state._infinite_supply)
    if keyboard.get_key_down('f6'):
        state._controlling_ugv -= 1
        if state._controlling_ugv < 1:
            state._controlling_ugv = 1
    if keyboard.get_key_down('f7'):
        state._controlling_ugv += 1

    if keyboard.get_key_down('e'):
        cmd_ugv.start_motor(state._controlling_ugv)
    if keyboard.get_key_down('q'):
        cmd_ugv.stop_motor(state._controlling_ugv)

    if keyboard.get_key_down('+'):
        cmd_ugv.set_gear(state._controlling_ugv, True)
    if keyboard.get_key_down('-'):
        cmd_ugv.set_gear(state._controlling_ugv, False)

    if keyboard.get_key_down('o'):
        cmd_ugv.set_handbrake(state._controlling_ugv, True)
    if keyboard.get_key_down('l'):
        cmd_ugv.set_handbrake(state._controlling_ugv, False)

    if keyboard.get_key_down('0'):
        cmd_ugv.set_turn_choice(state._controlling_ugv, 0)
    if keyboard.get_key_down('1'):
        cmd_ugv.set_turn_choice(state._controlling_ugv, 1)

    if keyboard.get_key_down('t'):
        cmd_ugv.start_supply(state._controlling_ugv, state._subject_station, state.cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('g'):
        cmd_ugv.start_supply(state._controlling_ugv, state._subject_station, state.cmd_interop.SUPPLY_WATER)
    if keyboard.get_key_down('y'):
        cmd_ugv.stop_supply(state._controlling_ugv, cmd_interop.SUPPLY_FUEL)
    if keyboard.get_key_down('h'):
        cmd_ugv.stop_supply(state._controlling_ugv, cmd_interop.SUPPLY_WATER)

    # Firehose pressure
    if keyboard.get_key_down('d'):
        state._fire_hose_pressure += 0.5
        cmd_ugv.adjust_firehose(state._controlling_ugv, state._fire_hose_pressure)
    if keyboard.get_key_down('a'):
        state._fire_hose_pressure -= 0.5
        if state._fire_hose_pressure < 0:
            _fire_hose_pressure = 0
        cmd_ugv.adjust_firehose(state._controlling_ugv, _fire_hose_pressure)

    # Firehose direction
    if keyboard.get_key_down('z'):
        state._fire_hose_dir[0] -= 1
        update_firehose()
    if keyboard.get_key_down('x'):
        state._fire_hose_dir[0] += 1
        update_firehose()
    if keyboard.get_key_down('c'):
        state._fire_hose_dir[1] -= 1
        update_firehose()
    if keyboard.get_key_down('v'):
        state._fire_hose_dir[1] += 1
        update_firehose()
    if keyboard.get_key_down('b'):
        state._fire_hose_dir[2] -= 1
        update_firehose()
    if keyboard.get_key_down('n'):
        state._fire_hose_dir[2] += 1
        update_firehose()

    if keyboard.get_key_down('f11'):
        state._subject_station -= 1
        if state._subject_station < 1:
            state._subject_station = 1
    if keyboard.get_key_down('f12'):
        state._subject_station += 1

    cmd_ugv.set_throttle(state._controlling_ugv, 1 if keyboard.get_key('w') else 0)
    cmd_ugv.set_brake(state._controlling_ugv, 1 if keyboard.get_key('s') else 0)