"""Class for making a rule object that represents an arc along with head- and tail-node"""


def is_digit(signal):
    """function for checking if the signal is a digit (0-9)"""
    return 48 <= ord(str(signal)) <= 57


def is_digit_0_5(signal):
    """function for checking if the signal is a digit (0-5)"""
    return 48 <= ord(str(signal)) <= 53


def any_signal(signal):
    """function for checking if the signal is any value"""
    return True


def is_astrix(signal):
    """function for checking if the signal is an astrix"""
    return signal == '*'


def is_hashtag(signal):
    """function for checking if the signal is a hashtag"""
    return signal == '#'


def is_yes(signal):
    """function for checking if the signal is YES"""
    return signal == 'Y'


class Rule:
    """function for making Rule object with head- and tail-states, signal and action"""
    def __init__(self, state1, state2, signal, action):
        """initiating four instance variables"""
        self.state1 = state1  # triggering state
        self.state2 = state2  # new state if rule fires
        self.signal = signal  # triggering signal
        self.action = action  # action performed if rule fires

