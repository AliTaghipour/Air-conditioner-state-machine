class Device(object):
    def __init__(self, name):
        self.name = name
        self.activation = False
        self.speed = 4

    def turn_on(self):
        if self.activation:
            print(self.name + " already turned on")
        else:
            self.activation = True
            print("Turning on " + self.name)

    def turn_off(self):
        if not self.activation:
            print(self.name + " already turned off")
        else:
            self.activation = False
            print("Turning off " + self.name)

    def set_speed(self, speed):
        print(self.name, " speed set to:", self.speed)
        self.speed = speed
