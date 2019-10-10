"""The controller."""
import ledboard
import keypad
import fsm
import rule


class KPCAgent:
    """Coordinates between the other classes, verifies and changes passwords."""

    def __init__(self):
        print("Hello world!")
        self.ledboard = ledboard.Ledboard()
        print("Bye world")
        self.keypad = keypad.KeyPad()
        self.fsm = fsm.FSM(self)
        self.filename = "password.txt"
        self.passcode = None
        self.cum_pc = ""
        self.last_signal = ""
        self.override = None
        self.lid = None
        self.ldur = ""
        self.new_password = ""

        self.add_rules()
        # Tries to read from the password file
        try:
            file = open(self.filename, "r")
            self.passcode = file.readlines()[-1]
            file.close()
        except FileNotFoundError:
            pass
        finally:
            self.fsm.main_loop()

    def add_rules(self):
        """Adds rules to the fsm in the correct order"""
        self.fsm.add_rule(
            rule.Rule(
                fsm.INIT,
                fsm.READ,
                rule.any_signal,
                self.init_passcode_entry))
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ,
                fsm.READ,
                rule.is_digit,
                self.save_digit))
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ,
                fsm.VERIFY,
                rule.is_astrix,
                self.verify_login))
        #self.fsm.add_rule(
         #   rule.Rule(
          #      fsm.READ,
           #     fsm.INIT,
            #    rule.any_signal,
             #   self.init_passcode_entry))
        self.fsm.add_rule(
            rule.Rule(
                fsm.VERIFY,
                fsm.ACTIVE,
                rule.is_yes,
                self.twinkle_leds()))
        self.fsm.add_rule(
            rule.Rule(
                fsm.VERIFY,
                fsm.INIT,
                rule.any_signal,
                self.failed_login))
        self.fsm.add_rule(
            rule.Rule(
                fsm.ACTIVE,
                fsm.READ_2,
                rule.is_astrix,
                self.refresh_agent))  # enter R-2
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_2,
                fsm.READ_2,
                rule.is_digit,
                self.save_digit))  # enters new password
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_2,
                fsm.READ_3,
                rule.is_astrix,
                self.cache_passcode))  # save first trial
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_2,
                fsm.ACTIVE,
                rule.any_signal,
                self.refresh_agent))  # wrong entry
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_3,
                fsm.READ_3,
                rule.is_digit,
                self.save_digit))  # enters new password
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_3,
                fsm.ACTIVE,
                rule.is_astrix,
                self.validate_passcode_change))
        self.fsm.add_rule(
            rule.Rule(
                fsm.READ_3,
                fsm.ACTIVE,
                rule.any_signal,
                self.refresh_agent))  # wrong entry
        self.fsm.add_rule(
            rule.Rule(
                fsm.ACTIVE,
                fsm.LED,
                rule.is_digit_0_5,
                self.choose_led))  # choose led 0-5
        self.fsm.add_rule(
            rule.Rule(
                fsm.LED,
                fsm.TIME,
                rule.is_astrix,
                self.empty_method))  # enters time-state
        self.fsm.add_rule(
            rule.Rule(
                fsm.LED,
                fsm.ACTIVE,
                rule.any_signal,
                self.refresh_agent))  # wrong entry
        self.fsm.add_rule(
            rule.Rule(
                fsm.TIME,
                fsm.TIME,
                rule.is_digit,
                self.save_ldur))  # enters duration of LED-high
        self.fsm.add_rule(
            rule.Rule(
                fsm.TIME,
                fsm.ACTIVE,
                rule.is_astrix,
                self.light_one_led))  # light LED
        self.fsm.add_rule(
            rule.Rule(
                fsm.TIME,
                fsm.ACTIVE,
                rule.any_signal,
                self.refresh_agent))  # wrong entry
        self.fsm.add_rule(
            rule.Rule(
                fsm.ACTIVE,
                fsm.LOGOUT,
                rule.is_hashtag,
                self.empty_method))  # begin logout
        self.fsm.add_rule(
            rule.Rule(
                fsm.LOGOUT,
                fsm.DONE,
                rule.is_hashtag,
                self.exit_action))  # confirm logout

    def cache_passcode(self):
        """saves passcode after first trial"""
        self.new_password = self.cum_pc
        self.cum_pc = ""

    def refresh_agent(self):
        """resets cum_pc and ldur in case of passcode-change and led-activation"""
        self.cum_pc = ""
        self.ldur = ""

    def choose_led(self):
        """Designates the led pin"""
        self.lid = self.last_signal

    def save_ldur(self):
        """update ldur with signal from keypad"""
        self.ldur += str(self.last_signal)

    def init_passcode_entry(self):
        """"Clears the passcode-buffer and init 'power up' lights.
        Used when user first presses the keypad"""
        self.cum_pc = ""
        self.ledboard.power_up()

    def failed_login(self):
        """Flashes lights and calls init_passcode_entry"""
        self.flash_leds()
        self.init_passcode_entry()

    def get_next_signal(self):
        """returns override signal if it's not blank.
        Otherwise returns the next signal from the keypad"""
        if self.override:
            temp = self.override
            self.override = None
            return temp
        self.last_signal = self.keypad.get_next_signal()
        return self.last_signal

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
        if len(self.cum_pc) >= 4 and self.cum_pc.isdigit(
        ) and self.cum_pc == self.new_password:
            file = open(self.filename, "w+")
            file.write(self.cum_pc)
            file.close()
            self.passcode = self.cum_pc
            self.ledboard.changed_password_success()
        else:
            self.ledboard.changed_password_fail()

    def save_digit(self):
        """Adds the digit to the cumulative password"""
        self.cum_pc += str(self.last_signal)

    def light_one_led(self):
        """Calls Ledboard to turn LED #self.lid be turned on for self.ldur sek"""
        self.ledboard.light_led(self.lid, int(self.ldur))
        self.lid = 0
        self.ldur = ""

    def flash_leds(self):
        """Calls ledboard to flash all LEDs for 1 sek"""
        self.ledboard.flash_all_leds(1)

    def twinkle_leds(self):
        """Calls ledboard to twinkle all LEDs for 2 sek"""
        self.ledboard.twinkle_all_leds(2)

    def exit_action(self):
        """Calls ledboard to init 'power down' light sequence"""
        self.ledboard.power_down()

    def empty_method(self):
        """Dummy method"""


def main():
    KPCAgent()


if __name__ == "__main__":
    main()
