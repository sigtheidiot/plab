"""The controller."""
import ledboard
import keypad
import fsm


class KPCAgent():
    """Coordinates between the other classes, verifies and changes passwords."""
    def __init__(self):
        self.ledboard = ledboard.Ledboard()
        self.keypad = keypad.KeyPad()
        self.fsm = fsm.FSM(self)
        self.filename = "password.txt"
        self.passcode = None
        self.cum_pc = ""
        self.override = None
        self.lid = None
        self.ldur = None
        # Tries to read from the password file
        try:
            file = open(self.filename, "r")
            self.passcode = file.readlines()[-1]
            file.close()
        except FileNotFoundError:
            "nothing"

    def init_passcode_entry(self):
        """Clears the passcode-buffer and init 'power up' lights.
        Used when user first presses the keypad"""
        self.cum_pc = ""
        self.ledboard.power_up()

    def get_next_signal(self):
        """returns override signal if it's not blank.
        Otherwise returns the next signal from the keypad"""
        if self.override:
            temp = self.override
            self.override = None
            return temp
        return self.keypad.get_next_signal()

    def verify_login(self):
        """Checks if the password entered matches registered password.
        Stores the result ('Y' or 'N') in the override signal.
        init correct light sequence"""
        if self.cum_pc == self.passcode:
            self.ledboard.changed_password_success()
            return 'Y'
        self.ledboard.changed_password_fail()
        return 'N'

    def validate_passcode_change(self):
        """Checks that the new password is legal (>= 4 digits).
        If so, writes the new password to file.
        init correct light sequence."""
        if len(self.cum_pc) >= 4 and self.cum_pc.isdigit():
            file = open(self.filename, "w+")
            file.write(self.cum_pc)
            file.close()
            self.passcode = self.cum_pc
            self.ledboard.changed_password_success()
        else:
            self.ledboard.changed_password_fail()

    def save_digit(self, digit):
        """Adds the digit to the cumulative password"""
        self.cum_pc += digit

    def light_one_led(self):
        """Calls Ledboard to turn LED #self.lid be turned on for self.ldur sek"""
        self.ledboard.light_led(self.lid, self.ldur)

    def flash_leds(self):
        """Calls ledboard to flash all LEDs"""
        self.ledboard.flash_all_leds()

    def twinkle_leds(self):
        """Calls ledboard to twinkle all LEDs"""
        self.ledboard.twinkle_all_leds()

    def exit_action(self):
        """Calls ledboard to init 'power down' light sequence"""
        self.ledboard.power_down()
