import machine

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
buzzer.bip(0.1)



while running:
    try:
        wifi.checkIsConnected()
        mqtt.subscribeToTopic('crf92')
        utime.sleep(1)
    except:
        machine.soft_reset()


