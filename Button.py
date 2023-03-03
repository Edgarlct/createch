import machine

class Button:
    def __init__(self):
        self.button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

    def MainIsPressed(self):
        return self.button.value() == 1