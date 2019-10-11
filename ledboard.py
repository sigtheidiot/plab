"""file for the ledboard class"""
from time import sleep, time
import RPi.GPIO as GPIO


class Ledboard:
    """Class for ledboard"""

    pins = [26, 19, 13]
    pin_led_states = [
        [1, 0, -1],
        [0, 1, -1],
        [1, -1, 0],
        [0, -1, 1],
        [-1, 1, 0],
        [-1, 0, 1]]

    def __init__(self):
        """Set the proper mode """
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        """Sets the pin"""
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def turn_on_led(self, led_nr):
        """Turns on spesific led by calling set_pin"""
        for pin_index, pin_state in enumerate(self.pin_led_states[led_nr]):
            self.set_pin(pin_index, pin_state)

    def turn_off_all_leds(self):
        """Turns off all leds"""
        self.set_pin(0, -1)
        self.set_pin(1, -1)
        self.set_pin(2, -1)

    def light_led(self, led, sec):
        """Turns on the led by calling the turn_on_led function,
        then calls the sleep function with paramater time. Then turns off all leds"""
        self.turn_on_led(led)
        sleep(sec)
        self.turn_off_all_leds()

    def flash_all_leds(self, sec):
        """Flash all 6 LEDs on and off for a specified number of seconds,
        defined by the sec argument"""
        endtime = time() + sec
        while time() < endtime:
            for index in range(2):
                self.turn_on_led(index)
                sleep(0.01)
            self.turn_off_all_leds()
            sleep(0.2)
        self.turn_off_all_leds()

    def twinkle_all_leds(self, sec):
        """Turn all LEDs on and off in sequence for a specified
        number of seconds, defined by the sec argument"""
        endtime = time() + sec
        while time() < endtime:
            for index in range(2,4):
                self.turn_on_led(index)
                sleep(0.5)
            self.turn_off_all_leds()
            sleep(0.2)
        self.turn_off_all_leds()

    def power_up(self):
        """Turn on the power up sequence"""
        order = [0, 2, 4, 5, 3, 1]
        for index in order:
            self.turn_on_led(index)
            sleep(0.5)
        self.turn_off_all_leds()

    def power_down(self):
        """Turn on the power down sequence"""
        order = [1, 3, 5, 4, 2, 0]
        for index in order:
            self.turn_on_led(index)
            sleep(0.5)
        self.turn_off_all_leds()

    def changed_password_fail(self):
        """Turn on the login fail sequence"""
        order = [5, 4, 1, 0]
        for index in order:
            self.turn_on_led(index)
            sleep(0.5)
        self.turn_off_all_leds()

    def changed_password_success(self):
        """Turn on the changed password success sequence"""
        order = [5, 4, 2, 3]
        for index in order:
            self.turn_on_led(index)
            sleep(0.5)
        self.turn_off_all_leds()
