class State(object):
    def __init__(self, name, heater, cooler, state_job):
        self.name = name
        self.heater = heater
        self.cooler = cooler
        self.state_job = state_job
        self.states_dict = None

    def set_states_dict(self, states_dict):
        self.states_dict = states_dict

    def get_next_state(self, event):
        if event in self.states_dict.keys():
            return self.states_dict.get(event)

        return self

    def run_job(self):
        self.state_job(self.cooler, self.heater)
