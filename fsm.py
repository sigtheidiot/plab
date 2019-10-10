"""Class for making an FSM object with associated methods"""
import kpc_agent

INIT = 's_init'
READ = 's_read'
VERIFY = 's_verify'
ACTIVE = 's_active'
READ_2 = 's_read2'
READ_3 = 's_read3'
LED = 's_led'
TIME = 's_time'
LOGOUT = 's_logout'
DONE = 's_done'


class FSM:
    """Class for making Final-state-machine"""
    def __init__(self, agent):
        self.agent = agent
        self._rule_list = []
        self.state = INIT

    def add_rule(self, this_rule):
        """add a new rule-object to the end of rule_list"""
        self._rule_list.append(this_rule)

    def get_next_signal(self):
        """gets next_signal from agent"""
        return self.agent.get_next_signal()

    def run_rules(self):
        """apply each rule in rule_list until one is fired"""
        next_signal = self.get_next_signal()
        for this_rule in self._rule_list:
            if self.apply_rule(this_rule, next_signal):  # if rules conditions is passed
                self.fire_rule(this_rule)  # rule is fired

    def apply_rule(self, this_rule, next_signal):
        """check if conditions of rule are met"""
        return this_rule.state1 == self.state and this_rule.signal(next_signal)

    def fire_rule(self, this_rule):
        """"sets next_state equal head-state of the rule that is
         fired and calls the agent-method given by the rule"""
        self.state = this_rule.state2
        this_rule.action()

    def main_loop(self):
        """begins in initial state and call get_next_signal and
         run_rules until FSM enters final state"""
        print(self.state)
        while self.state != DONE:
            # self.get_next_signal()  run_rules() calls get_next_signal
            self.run_rules()
            print(self.state)
