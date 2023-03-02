import machine

from Button import Button
from Buzzer import Buzzer
from Message import Message
from Screen import Screen
from Wifi import Wifi
import utime


###################################################################
####################### GLOBAL STATE VARIABLES ####################
###################################################################

####################### DEVICE STATE ##############################

DEVICE_STATE = "home"
""" can be "home", "sleeping", "alerting", "readingMessage"""
RUNNING = True
""":type: bool, value: True or False  does the program run or not"""

######### wifi ##########
WIFI_STATUS = "disconected"
""":type: str, value: "connected" or "disconnected" """

########## MQTT ##########
MQTT_STATUS = "disconected"
""":type: str, value: "connected" or "disconnected" or "connecting" """

MQTT_SUBSCRIBED_TOPIC = "none"
""" :type: str, value: "none" or <topic name> """

########## BUTTONS ##########
MAIN_BUTTON_PRESSED = False
""" :type: bool, value: True or False """

SECOND_BUTTON_STATUS = False
""" :type: bool, value: True or False """

########## SCREEN ##########
SCREEN_ON = True

########## ALARM ##########
ALARM_STATUS = "stoped"
""":type: str, value: "stoped" "called" or "ringing" """

########## RECEIVED_MESSAGES ##########
RECEIVED_MESSAGE_CUE = []
""":type: list, value: {"message": sting, targets: [string] } 
    targets are the array containing device uuids of message targets, can be all to broadcast to all devices
    example: {"message": "hello", targets: ["ATY72", "all"]}
"""


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


###################################################################
####################### MAIN LOOP #################################
###################################################################

while RUNNING:
    try:
        wifi.checkIsConnected()
        mqtt.subscribeToTopic('crf92')
        utime.sleep(1)
    except:
        machine.soft_reset()


