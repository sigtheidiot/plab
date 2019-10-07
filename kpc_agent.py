"""The controller."""


class KPCAgent():
    """Coordinates between the other classes, verifies and changes passwords."""
    def __init__(self):
        return

    def init_passcode_entry(self):
        """Clears the passcode-buffer and init 'power up' lights.
        Used when user first presses the keypad"""

    def get_next_signal(self):
        """returns override signal if it's not blank.
        Otherwise returns the next signal from the keypad(?)"""

    def verify_login(self):
        """Checks if the password entered matches registered password.
        Stores the result ('Y' or 'N') in the override signal.
        init correct light sequence"""

    def validate_passcode_change(self):
        """Checks that the new password is legal.
        If so, writes the new password to file.
        init correct light sequence."""

    def light_one_led(self):
        """Calls Ledboard to turn LED #self.lid be turned on for self.ldur sek"""

    def flash_leds(self):
        """Calls ledboard to flash all LEDs"""

    def twinkle_leds(self):
        """Calls ledboard to twinkle all LEDs"""

    def exit_action(self):
        """Calls ledboard to init 'power down' light sequence"""
