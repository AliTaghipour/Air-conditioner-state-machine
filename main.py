import random
import time

from model.Device import Device
from model.Event import Event
from model.State import State
from model.SuperState import SuperState

HeaterDeviceName = "Heater"
HeaterActivation = False
CoolerDeviceName = "Cooler"
CoolerActivation = False

Under40 = "t<40"
Under35 = "t<35"
Under25 = "t<25"
Under15 = "t<15"
Higher45 = "t>45"
Higher40 = "t>40"
Higher35 = "t>35"
Higher30 = "t>30"

events = [Under15, Under25, Higher30, Under35, Higher35, Under40, Higher40, Higher45]


def state_s1_handler(cooler, heater):
    cooler.turn_off()
    heater.turn_off()


def state_s2_handler(cooler, heater):
    cooler.turn_on()
    heater.turn_off()


def state_s2_s1_handler(cooler, heater):
    cooler.set_speed(4)


def state_s2_s2_handler(cooler, heater):
    cooler.set_speed(6)


def state_s2_s3_handler(cooler, heater):
    cooler.set_speed(8)


def state_s3_handler(cooler, heater):
    cooler.turn_off()
    heater.turn_on()


def void(cooler, heater):
    pass


def start():
    event_handler = Event(1, events, 3)
    heater = Device(HeaterDeviceName)
    cooler = Device(CoolerDeviceName)

    state1 = State("s1", heater, cooler, state_s1_handler)

    state21 = State("s2-s1", heater, cooler, state_s2_s1_handler)
    state22 = State("s2-s2", heater, cooler, state_s2_s2_handler)
    state23 = State("s2-s3", heater, cooler, state_s2_s3_handler)
    final_state_s2 = State("s3-final", heater, cooler, void)
    state21.set_states_dict({Under25: final_state_s2, Higher40: state22})
    state22.set_states_dict({Under35: state21, Higher45: state23})
    state23.set_states_dict({Under40: state22})
    final_state_s2.set_states_dict({Under25: state1})

    state2_super_state = SuperState("s2", state21, final_state_s2, event_handler.get_next_event)

    state3 = State("s3", heater, cooler, state_s3_handler)
    final_state = State("final", heater, cooler, state_s3_handler)

    state1.set_states_dict({Under15: state3, Higher35: state2_super_state})
    state3.set_states_dict({Higher30: state1})

    super_state = SuperState("S", state1, final_state, event_handler.get_next_event)
    super_state.get_next_state("")


start()
