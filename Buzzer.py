import machine
import utime


class Buzzer:

    def __init__(self):
        self.buzzer = machine.PWM(machine.Pin(15, mode=machine.Pin.OUT))
        # self.buzzerBip = machine.Pin(2, machine.Pin.OUT)
        self.bip(0.2, 2)
        utime.sleep(0.1)
        self.buzzer.freq(1000)
        self.tones = {"B4": 493.88,"C#5/Db5": 554.37,"E5": 659.25}

    def playtone(self, frequency):
        self.buzzer.duty_u16(60000)
        self.buzzer.freq(int(frequency))

    def bequiet(self):
        self.buzzer.duty_u16(0)

    def bip(self, delay, rep = 1):
        for i in range(rep):
            print('bip')
            # self.buzzerBip.on()
            utime.sleep(delay)
            # self.buzzerBip.off()
            utime.sleep(delay)
        return

    def playAlert(self):
        music = ["E5", "E5", "C#5/Db5","C#5/Db5", "P", "C#5/Db5","C#5/Db5","P", "B4","B4", "C#5/Db5","C#5/Db5", "E5","E5", "P"]
        for i in range(len(music)):
            if music[i] == "P":
                self.bequiet()
            else:
                self.playtone(self.tones[music[i]])
            utime.sleep(0.08)
        self.bequiet()
        return