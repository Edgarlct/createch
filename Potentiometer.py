import machine

class Potentiometer:
    def __init__(self):
        self.pot1 = machine.Pin(14)
        self.pot2 = machine.Pin(13)
        self.pot3 = machine.Pin(12)