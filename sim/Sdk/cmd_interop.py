import sys
import socket
import select
import json

# ================================================ PRIVATE CONSTANTS ================================================

_CLIENT_ADDRESS = "127.0.0.1"
_CLIENT_PORT = 10801
_SERVER_ADDRESS = "127.0.0.1"
_SERVER_PORT = 10802

_RECEIVE_TIMEOUT = 20

_INT_MSG_TYPE__UGV_CONTROL = 1

# ================================================ PRIVATE VARIABLES ================================================

_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
_socket.bind((_CLIENT_ADDRESS, _CLIENT_PORT))
_socket.setblocking(False)


# ================================================ PRIVATE FUNCTIONS ================================================

def _send_message(data):
    _socket.sendto(data, (_SERVER_ADDRESS, _SERVER_PORT))


def _decode_message(message):
    if message is None:
        return None
    if len(message) == 0:
        return None
    return json.loads(message.decode('utf8'))


# ================================================ PUBLIC CONSTANTS ================================================

SUPPLY_FUEL = 1
SUPPLY_WATER = 2

# ================================================ PUBLIC FUNCTIONS ================================================


def send_message(data_list):
    _send_message(bytearray(data_list))


def receive_message():
    data = None
    try:
        ready = select.select([_socket], [], [], _RECEIVE_TIMEOUT / 1000.0)
        if ready[0]:
            data = _socket.recv(65535)
    except Exception as e:
        print(e, file=sys.stderr)
    return _decode_message(data)
