import pynput

_current = {}
_prev = {}

_key_down = {}
_key_up = {}


def _on_press(key):
    try:
        _current[key.char] = True
    except:
        try:
            _current[key.name] = True
        except:
            pass
        pass


def _on_release(key):
    try:
        del _current[key.char]
    except:
        try:
            del _current[key.name]
        except:
            pass
        pass


_listener = pynput.keyboard.Listener(
    on_press=_on_press,
    on_release=_on_release)
_listener.start()


def perform_update():
    global _key_down
    global _key_up
    global _prev

    _key_down = {}
    _key_up = {}

    for i in _prev:
        if not (i in _current):
            _key_up[i] = True
    for i in _current:
        if not (i in _prev):
            _key_down[i] = True

    _prev = dict(_current)


def get_key(c):
    return c in _current


def get_key_down(c):
    return c in _key_down


def get_key_up(c):
    return c in _key_up
