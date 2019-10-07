"""Class for making a rule object that represents an arc along with head- and tail-node"""


class Rule:
    def __init__(self, state1, state2, signal, action):
        """initiating four instance variables"""
        self.state1 = state1  # triggering state
        self.state2 = state2  # new state if rule fires
        self.signal = signal  # triggering signal
        self.action = action  # action performed if rule fires


def signal_is_digit(signal):
    """function for checking if the signal is a digit (0-9)"""
    return 48 <= ord(signal) <= 57






