# this class is used for the interaction with the screen
from machine import I2C, Pin
from lib.ssd1306 import SSD1306_I2C
import framebuf


class Screen:
    def __init__(self):
        self.i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)
        self.oled = SSD1306_I2C(128, 64, self.i2c)
        self.oled.fill(0)
        self.oled.show()

    def showWifiConnected(self):
        self.oled.fill(0)
        # load the image from the bit array
        bitmap = bytearray(b'\x00\x00\x00\x00\x00\x00\x01\xf8\x00\x0f\xff\x00\x3e\x07\xc0\x70\x00\xe0\xe3\xfc\x70\xc7\xfe\x30\x1e\x07\x80\x18\x01\x80\x11\xf8\x80\x03\xfc\x00\x07\x0e\x00\x04\x62\x00\x00\xf0\x00\x00\xf0\x00\x00\xf0\x00\x00\x60\x00\x00\x00\x00\x00\x00\x00\x00')
        fbuf = framebuf.FrameBuffer(bitmap, 20, 16, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, 0, 0)

        self.oled.show()

    def showWifiConnecting(self):
        self.oled.fill(0)
        bitmap = bytearray(b'\x00\x00\x00\x00\x00\x00\x30\x00\x00\x39\xfe\x00\x1c\x07\x80\x3e\x01\xc0\x27\x38\x40\x07\x9e\x00\x0d\xc3\x00\x00\xe0\x00\x01\xf0\x00\x01\x38\x00\x00\x1c\x00\x00\xfe\x00\x00\xf7\x00\x00\xf3\x80\x00\xf1\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00')
        fbuf = framebuf.FrameBuffer(bitmap, 20, 16, framebuf.MONO_HLSB)
        self.oled.blit(fbuf, 0, 0)
        self.oled.show()
