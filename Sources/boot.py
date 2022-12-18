import supervisor
import board
import storage
import usb_cdc

from digitalio import DigitalInOut, Direction, Pull

supervisor.set_next_stack_limit(4096 + 4096)

row = DigitalInOut(board.GP3)
col = DigitalInOut(board.GP4)

row.direction = Direction.INPUT
col.direction = Direction.OUTPUT

row.pull = Pull.DOWN
col.value = True

# Wenn die Taste NICHT gedrückt ist wird alles abgeschaltet
# Nur wenn die Taste (#) gedrückt wird erscheint der serielle Port & das Laufwerk
if not row.value:
    # USB Laufwerk einblenden auf Knopfdruck (#)
    #storage.disable_usb_drive()
    # Seriellen Port einblenden auf Knopfdruck (#)
    #usb_cdc.disable()