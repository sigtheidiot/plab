"""file for the ledboard class"""

import RPi.GPIO as GPIO

class ledboard:
    """Class for ledboard"""

    def __init__(self):
        """Set the proper mode via: GPIO.setmode(GPIO.BCM)"""
        return

    def light_led(self, led, time):
        """Turn on one of the 6 LEDs by making the appropriate combination of input and
            output declarations, and then making the appropriate HIGH / LOW settings on the output
            pins."""
        return

    def flash_all_leds(self, time):
        """Flash all 6 LEDs on and off for a specified number of seconds, defined by the time argument"""
        return

    def twinkle_all_leds(self, time):
        """Turn all LEDs on and off in sequence for a specified number of seconds, defined by the time argument"""
        return

    def power_up(self):
        """Turn on the power up sequence"""
        return

    def power_down(self):
        """Turn on the power down sequence"""
        return

    def changed_password_fail(self):
        """Turn on the login fail sequence"""
        return

    def changed_password_success(self):
        """Turn on the changed password success sequence"""
        return


