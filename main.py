from Message import Message
from Screen import Screen
from Wifi import Wifi
import machine
import utime

screen = Screen()
wifi = Wifi("IIM_Private", "Creatvive_Lab_2023", screen)
# wifi = Wifi("iPhone de Edgar", "edouardlecon", screen)
message = Message(screen)

wifi.connect()





