"""Keypad functionality"""
import time
import RPi.GPIO as GPIO


class KeyPad:
    """Polls the keypad to detect keystrokes and sends them to the controller.
    Defines the correct pins"""

    def __init__(self):
        """Defines the correct pins and the symbols. Sets the keypad mode, and pin modes"""
        self.symbols = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        self.row_pins = [18, 23, 24, 25]
        self.col_pins = [17, 27, 22]
        GPIO.setmode(GPIO.BCM)
        # Set the row pin modes to output
        for row_pin in self.row_pins:
            GPIO.setup(row_pin, GPIO.OUT)
        # Set the col pin modes to pull down (Key push will cause HIGH signal)
        for col_pin in self.col_pins:
            GPIO.setup(col_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def do_polling(self):
        """Determines which key is being pressed"""
        for row_pin in self.row_pins:
            GPIO.output(row_pin, GPIO.HIGH)
            for col_pin in self.col_pins:
                # Checks if the col pin is actually high by checking 20 times
                # in 10 ms intervals
                i = 0
                while GPIO.input(col_pin) == GPIO.HIGH:
                    i += 1
                    if i >= 20:
                        return self.symbols[self.row_pins.index(row_pin)][self.col_pins.index(
                            col_pin)]
                    time.sleep(0.01)
            GPIO.output(row_pin, GPIO.LOW)
        return None

    def get_next_signal(self):
        """Interfaces with the controller.
        Repeatedly polls the keypad until a key is pressed.
        Returns an int or one of the chars '*' or '#'."""
        print("reached keypad before loop")
        key = None
        while key == None:
            key = self.do_polling()
        print("key: " + str(key))
        print("reached keypad after loop")
        return key
