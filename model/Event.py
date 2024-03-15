import random
import time


class Event(object):
    def __init__(self, id, events, initial_event_index):
        self.id = id
        self.events = events
        self.current_event_index = initial_event_index

    def get_next_event(self):
        time.sleep(1)
        r = random.random()
        index = self.current_event_index
        if r < 0.5:
            if index + 1 < len(self.events):
                index += 1
        else:
            if index - 1 >= 0:
                index -= 1
        self.current_event_index = index
        result = self.events[index]
        print("------------")
        print("event:", result)
        return result
