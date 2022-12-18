import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import send_string, simple_key_sequence
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.statusled import statusLED
from kmk.extensions.international import International

# Keyboard Instanz erzeugen
keyboard = KMKKeyboard()

# Debugging
keyboard.debug_enabled = True

# LED Konfig für Layer 1..3
statusLED = statusLED(led_pins=[board.GP14, board.GP26, board.GP15])

# Setup
media_keys = MediaKeys()
layers = Layers()
encoders = EncoderHandler()
keyboard.modules = [layers, encoders] 
keyboard.extensions.append(media_keys)
keyboard.extensions.append(statusLED)
keyboard.extensions.append(International())

# Tastatur Matrix
keyboard.col_pins = (board.GP2, board.GP0, board.GP4)
keyboard.row_pins = (board.GP1, board.GP6, board.GP5, board.GP3)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Encoder (Pin A, Pin B, Pin Button)
encoders.pins = (
                    (board.GP9, board.GP10, board.GP11, False),
                    # Second Encoder
                ) 

# Keymaps
keyboard.keymap = [
    # Windows
    [
        KC.MEDIA_PREV_TRACK,
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
        KC.DF(1)
    ],
    # OBS
        [
        KC.F13,
        KC.F14,
        KC.F15,
        KC.F16,
        KC.F17,
        KC.F18,
        KC.F19,
        KC.F20,
        KC.F21,
        KC.F22,
        KC.F23,
        KC.DF(2)
    ],
    # Schnitt
    [
        KC.LCTRL(KC.C),
        KC.LCTRL(KC.V),
        KC.LCTRL(KC.X),
        KC.B,
        KC.R,
        KC.F,
        KC.LCTRL(KC.BSPACE),
        KC.LSHIFT(KC.S),
        KC.LCTRL(KC.N2),
        KC.COMMA,
        KC.DOT,
        KC.DF(0)
    ]
]

# Encoder                          
encoders.map = (
                 # Layer 1 -> nach dem , käme Encoder 2 wenn vorhanden  
                 ((KC.VOLD, KC.VOLU, KC.MUTE),), 
                 # Layer 2
                 ((KC.VOLD, KC.VOLU, KC.MUTE),), 
                 # Layer 3
                 ((KC.LCTRL(KC.LALT(KC.COMMA)), KC.LCTRL(KC.LALT(KC.DOT)), KC.LCTRL(KC.LSHIFT(KC.N7))),),
               )

if __name__ == '__main__':
    keyboard.go()