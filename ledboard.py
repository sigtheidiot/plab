"""file for the ledboard class"""
from time import sleep, time
import RPi.GPIO as GPIO

class Ledboard:
    """Class for ledboard"""

    pins = [18, 23, 24]
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

        return

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


    def light_led(self, led, time):
        """Turns on the led by calling the turn_on_led function,
        then calls the sleep function with paramater time. Then turns off all leds"""
        self.turn_on_led(led)
        sleep(time)
        self.turn_off_all_leds()

    def flash_all_leds(self, sec):
        """Flash all 6 LEDs on and off for a specified number of seconds, defined by the sec argument"""
        endtime = time() + sec
        while time() < endtime:
            for index in range(6):
                self.turn_on_led(index)
                sleep(0.01)
            self.turn_off_all_leds()
            sleep(0.2)
        self.turn_off_all_leds()



    def twinkle_all_leds(self, sec):
        """Turn all LEDs on and off in sequence for a specified number of seconds, defined by the sec argument"""
        endtime = time() + sec
        while time() < endtime:
            for index in range(6):
                self.turn_on_led(index)
                sleep(0.5)
            self.turn_off_all_leds()
            sleep(0.2)
        self.turn_off_all_leds()
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






