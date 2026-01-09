# IO pins
import board

# KMK core
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap

# Keyboard instance
keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# Pin definition (Key 1 → Key 4)
PINS = [board.D3, board.D4, board.D2, board.D1]

# No matrix, direct keypad
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Morse primitives:
# Key 1 → .
# Key 2 → -
# Key 3 → .-
# Key 4 → ..

keyboard.keymap = [
    [
        KC.MACRO(Tap(KC.DOT)),                     # Key 1: .
        KC.MACRO(Tap(KC.MINUS))),                  # Key 2: -
        KC.MACRO(Tap(KC.DOT), Tap(KC.MINUS))),     # Key 3: .-
        KC.MACRO(Tap(KC.DOT), Tap(KC.DOT))),       # Key 4: ..
    ]
]

if __name__ == "__main__":
    keyboard.go()