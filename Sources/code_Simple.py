import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string, simple_key_sequence

# Keyboard Instanz erzeugen
keyboard = KMKKeyboard()

# Debugging
keyboard.debug_enabled = True

# Setup
media_keys = MediaKeys()
keyboard.extensions.append(media_keys)

# Tastatur Matrix
keyboard.col_pins = (board.GP2, board.GP0, board.GP4)
keyboard.row_pins = (board.GP1, board.GP6, board.GP5, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymaps
keyboard.keymap = [
    # Windows
    [
        #KC.MEDIA_PREV_TRACK,
        send_string("http>&&www.heise.de;'[:\"{"),
        KC.MEDIA_PLAY_PAUSE,
        KC.MEDIA_NEXT_TRACK,
        KC.LGUI(KC.LSHIFT(KC.C)),
        KC.LALT(KC.SPACE),
        KC.LCTRL(KC.LSHIFT(KC.ESCAPE)),
        KC.LGUI(KC.LCTRL(KC.LEFT)),
        KC.LGUI(KC.LCTRL(KC.D)),
        KC.LGUI(KC.LCTRL(KC.RIGHT)),
        KC.LGUI(KC.L),
        KC.LCTRL(KC.LALT(KC.LSHIFT(KC.C))),
        KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
