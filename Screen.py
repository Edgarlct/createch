# this class is used for the interaction with the screen
from machine import I2C, Pin
from lib.ssd1306 import SSD1306_I2C
import framebuf
import utime


class Screen:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.oled.fill(0)
        self.oled.show()
        self.width = self.oled.width
        self.height = self.oled.height


    def showHome(self, wifiStatus, mqtt_status="disconnected", home_texts=[]):
        #clear screen
        self.oled.fill(0)

        #wifi icon
        if wifiStatus == 'connected':
            self.show_wifi_connected()
        else:
            self.show_wifi_unconected()
        #mqtt icon
        if mqtt_status == 'connected':
            self.show_connected_to_broker()

        #show text on 3 lines
        if len(home_texts) == 3:
            self.oled.text(home_texts[0], round((100 - (len(home_texts[0]) * 5.5)) / 2), 30)
            self.oled.text(home_texts[1], round((100 - (len(home_texts[1]) * 5.5)) / 2), 40)
            self.oled.text(home_texts[2], round((100 - (len(home_texts[2]) * 5.5)) / 2), 50)

        #show
        self.oled.show()



    def show_connected_to_broker(self):
        bitmap = bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xf0?\xff\xe0\x1f\xff\xe0\x1f\xff\xe0\x1f\xff\xe0\x1f\xff\xe0\x1f\xff\xf0?\xff\xff\xfc\x0f\xff\xf8\x07\xf9\xf8\x07\xf9\xf8\x07\xff\xf8\x07\xff\xf8\x07\xf9\x98\x07\xf9\x98\xc7\xff\xf8\xc7\xff\xf8\x07\xff\xfc\x0f\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')
        fbuf = framebuf.FrameBuffer(bitmap, 20, 16, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, 110, 0)

    def show_wifi_connected(self):
        # load the image from the bit array
        bitmap = bytearray(b'\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x0f\xff\x00\x3e\x07\xc0\x70\x00\xe0\xe3\xfc\x70\xc7\xfe\x30\x1e\x07\x80\x18\x01\x80\x11\xf8\x80\x03\xfc\x00\x07\x0e\x00\x04\x62\x00\x00\xf0\x00\x00\xf0\x00\x00\xf0\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00')
        fbuf = framebuf.FrameBuffer(bitmap, 20, 16, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, 0, 0)

    def show_wifi_unconected(self):
        bitmap = bytearray(b'\x00\x00\x00\x00\x00\x00\x30\x00\x00\x39\xfe\x00\x1c\x07\x80\x3e\x01\xc0\x27\x38\x40\x07\x9e\x00\x0d\xc3\x00\x00\xe0\x00\x01\xf0\x00\x01\x38\x00\x00\x1c\x00\x00\xfe\x00\x00\xf7\x00\x00\xf3\x80\x00\xf1\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00')
        fbuf = framebuf.FrameBuffer(bitmap, 20, 16, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, 0, 0)

    def showMessage(self, message):
        letter_width = 9
        text_width = len(message) * letter_width
        utime.sleep(0.5)
        for i in range(text_width - self.width):
            self.oled.fill(0)
            self.oled.text(message[i // letter_width:], 0, (self.height // 2) - 4)
            self.oled.show()
            utime.sleep(0.010)

    def showUnreadMessage(self, button):
        self.oled.fill(0)
        bitmap = bytearray(b'\x00\x00\x18\x00\x00\x00\x00\x18\x00\x00\x00\x00\x18\x00\x00\x00\xc0\x18\x03\x00\x00\xe0\x18\x07\x00\x00\x70\x18\x0e\x00\x00\x70\x18\x0e\x00\x00\x38\x00\x1c\x00\x00\x18\x00\x18\x00\x00\x00\x3c\x00\x00\x00\x01\xff\x80\x00\x60\x07\xff\xe0\x06\x78\x0f\x00\xf0\x1e\x3e\x1e\x00\x78\x7c\x0e\x38\x00\x1c\x70\x00\x38\x00\x1c\x00\x00\x70\x00\x0e\x00\x00\x60\x00\x06\x00\x00\x60\x00\x06\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x00\xe0\x00\x07\x00\x07\xff\xff\xff\xe0\x07\xff\xff\xff\xe0\x06\x00\x00\x00\x60\x06\x00\x00\x00\x60\x06\x00\x00\x00\x60\x07\xff\xff\xff\xe0\x07\xff\xff\xff\xe0')
        fbuf = framebuf.FrameBuffer(bitmap, 40, 40, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, (self.width // 2) - 20, (self.height // 2) - 10)
        self.oled.show()
        # maybe one day I remove this shit
        happy_birthday = [
            "G4", "G4", "A4", "G4", "C5", "B4",
            "G4", "G4", "A4", "G4", "D5", "C5",
            "G4", "G4", "G5", "E5", "C5", "B4", "A4",
            "F5", "F5", "E5", "C5", "D5", "C5", "G4", "G4", "A4", "G4", "C5", "B4",
            "G4", "G4", "A4", "G4", "D5", "C5",
            "G4", "G4", "G5", "E5", "C5", "B4", "A4",
            "F5", "F5", "E5", "C5", "D5", "C5"
        ]


