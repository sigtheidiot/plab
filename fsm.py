"""Class for making an FSM object with associated methods"""
import Gruppeprosjekt.plab.rule as rule
import Gruppeprosjekt.plab.kpc_agent as kpc_agent


class FSM:
    def __init__(self, kpc_agent):
        self._agent = kpc_agent
        self._rule_list = []

    def add_rule(self, rule):
        self._rule_list.add(rule)

    def get_next_signal(self):
        return

    def run_rules(self):
        for rule in self._rule_list:
            if self.apply_rule(rule):
                self.fire_rule(rule)

    def apply_rule(self):
        return

    def fire_rule(self):
        return

    def main_loop(self):
        return





