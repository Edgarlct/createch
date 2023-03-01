import network
import utime


class Wifi:
    def __init__(self, ssid, password, screen):
        self.ssid = ssid
        self.password = password
        self.screen = screen
        self.wlan = network.WLAN(network.STA_IF)
        self.wlan.active(True)

    def connect(self):
        self.wlan.connect(self.ssid, self.password)
        self.checkIsConnected()

    def disconnect(self):
        self.wlan.disconnect()

    def checkIsConnected(self):
        while not self.wlan.isconnected():
            self.screen.showWifiConnecting()
            utime.sleep(1)
        self.screen.showWifiConnected()

