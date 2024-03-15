class SuperState(object):
    def __init__(self, name, initial_state, final_state, events_stream):
        self.name = name
        self.initial_state = initial_state
        self.final_state = final_state
        self.events_stream = events_stream

    def get_next_state(self, event):
        state = self.initial_state
        while state.name != self.final_state.name:
            state.run_job()
            print("current state:", state.name)
            event = self.events_stream()
            state = state.get_next_state(event)

        return self.final_state.get_next_state(event)

    def run_job(self):
        pass
