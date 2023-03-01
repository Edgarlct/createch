from Button import Button
from Buzzer import Buzzer
from Message import Message
from Screen import Screen
from Wifi import Wifi
import utime

running = True

from mqttClient import Mqtt

screen = Screen()
wifi = Wifi("IIM_Private", "Creatvive_Lab_2023", screen)
# wifi = Wifi("iPhone de Edgar", "edouardlecon", screen)
message = Message(screen)
message.displayMessage('welcome')
buzzer = Buzzer()
button = Button()
wifi.connect()

mqtt = Mqtt(message)

while running:
    mqtt.subscribeToTopic('crf92')
    utime.sleep(1)




screen.showUnreadMessage(buzzer, button)
message.displayMessage("VSPP1 depart dflekf sslekf jselkfjs elkfj elksjf ")




