"""Class for making an FSM object with associated methods"""
import rule
import kpc_agent

_init_state = 's_init'
_read_state = 's_read'
_verify_state = 's_verify'
_active_state = 's_active'
_led_state = 's_led'
_done_state = 's_done'


class FSM:
    def __init__(self, kpc_agent):
        self._agent = kpc_agent
        self._rule_list = []
        self.state = _init_state

    def add_rule(self, rule):
        """add a new rule-object to the end of rule_list"""
        self._rule_list.add(rule)

    def get_next_signal(self):
        """gets next_signal from agent"""
        return kpc_agent.get_next_signal()

    def run_rules(self):
        """apply each rule in rule_list until one is fired"""
        next_signal = self.get_next_signal()
        for this_rule in self._rule_list:
            if self.apply_rule(this_rule, next_signal):  # if rules conditions is passed
                self.fire_rule(this_rule)  # rule is fired

    def apply_rule(self, this_rule, next_signal):
        """check if conditions of rule are met"""
        return this_rule.state1 == self.state and this_rule.signal(next_signal)


    def fire_rule(self, rule):
        """"sets next_state equal head-state of the rule that is fired and calls the agent-method given by the rule"""
        self.state = rule.state2
        rule.action()


    def main_loop(self):
        """begins in initial state and call get_next_signal og run_rules until FSM enters final state"""

        self.state = _init_state
        while self.state != _done_state:
            self.get_next_signal()
            self.run_rules()
