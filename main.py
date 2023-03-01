from Button import Button
from Buzzer import Buzzer
from Message import Message
from Screen import Screen
from Wifi import Wifi
import utime

running = True

from mqttClient import Mqtt

screen = Screen()
wifi = Wifi("wiFiste", "CRF92!vps", screen)
# wifi = Wifi("iPhone de Edgar", "edouardlecon", screen)
messager = Message(screen)
messager.displayMessage('welcome')
utime.sleep(1)
button = Button()
wifi.connect()
buzzer = Buzzer()
mqtt = Mqtt(messager, button, buzzer)

while running:
    print('subscribe')
    mqtt.subscribeToTopic('crf92')
    utime.sleep(1)


