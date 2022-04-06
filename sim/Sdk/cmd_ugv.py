from . import cmd_interop
import struct


# ================================================ PRIVATE FUNCTIONS ================================================

def _send_cmd(ugv_id, cmd_type, p0, p1, p2):
    data = [2]
    for i in ugv_id.to_bytes(4, "big"):
        data.append(i)
    data.append(cmd_type.to_bytes(1, "big")[0])
    for i in struct.pack('>f', p0):
        data.append(i)
    for i in struct.pack('>f', p1):
        data.append(i)
    for i in struct.pack('>f', p2):
        data.append(i)
    cmd_interop.send_message(data)


# ================================================ PUBLIC FUNCTIONS ================================================


def start_motor(ugv):
    _send_cmd(ugv, 6, 0, 0, 0)


def stop_motor(ugv):
    _send_cmd(ugv, 7, 0, 0, 0)


def set_gear(ugv, is_forward):
    _send_cmd(ugv, 3, 1 if is_forward else 0, 0, 0)


def set_handbrake(ugv, is_active):
    _send_cmd(ugv, 4, 1 if is_active else 0, 0, 0)


def set_turn_choice(ugv, choice):
    _send_cmd(ugv, 5, choice, 0, 0)


def set_throttle(ugv, value):
    _send_cmd(ugv, 1, value, 0, 0)


def set_brake(ugv, value):
    _send_cmd(ugv, 2, value, 0, 0)


def start_supply(ugv, station, supply_type):
    _send_cmd(ugv, 8, station, supply_type, 0)


def stop_supply(ugv, supply_type):
    _send_cmd(ugv, 9, supply_type, 0, 0)


def align_firehose(ugv, dir_x, dir_y, dir_z):
    _send_cmd(ugv, 10, dir_x, dir_y, dir_z)


def adjust_firehose(ugv, pressure):
    _send_cmd(ugv, 11, pressure, 0, 0)
