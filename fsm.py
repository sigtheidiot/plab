"""Class for making an FSM object with associated methods"""
import rule
import kpc_agent


class FSM:
    def __init__(self, kpc_agent):
        self._agent = kpc_agent
        self._rule_list = []

    def add_rule(self, rule):
        """add a new rule-object to the end of rule_list"""
        self._rule_list.add(rule)

    def get_next_signal(self):
        """gets next_signal from agent"""
        kpc_agent.get_signal()

    def run_rules(self):
        """apply each rule in rule_list until one is fired"""
        for rule in self._rule_list:
            if self.apply_rule(rule):
                self.fire_rule(rule)

    def apply_rule(self):
        """check if conditions of rule are met"""
        return

    def fire_rule(self):
        """"depending on the rule will (1) set the next state and (2) call agent action method"""
        return

    def main_loop(self):
        """begins in initial state and call get_next_signal og run_rules until FSM enters final state"""
        state =



        while state !=






