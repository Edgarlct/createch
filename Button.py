import machine

class Button:
    def __init__(self):
        self.button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

    def isPressed(self):
        return self.button.value() == 0