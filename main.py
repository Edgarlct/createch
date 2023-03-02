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
WIFI_STATUS = "disconnected"
""":type: str, value: 'connected' or 'disconnected' 'connected_no_internet'"""

########## MQTT ##########
MQTT_STATUS = "disconected"
""":type: str, value: "connected" or "disconnected" """

MQTT_SUBSCRIBED_TOPIC = "none"
""" :type: str, value: "none" or <topic name> """

########## BUTTONS ##########
MAIN_BUTTON_PRESSED = False
""" :type: bool, value: True or False """

SECOND_BUTTON_STATUS = False
""" :type: bool, value: True or False """

########## SCREEN ##########
SCREEN_ON = True
""" :type: bool, value: True or False """

########## ALARM ##########
ALARM_STATUS = "stoped"
""":type: str, value: "stoped" "called" or "ringing" """

########## RECEIVED_MESSAGES ##########
RECEIVED_MESSAGE_CUE = []
""":type: list, value: {"message": sting, targets: [string] } 
    targets are the array containing device uuids of message targets, can be all to broadcast to all devices
    example: {"message": "hello", targets: ["ATY72", "all"]}
"""

########## TEXT ##########
HOME_TEXT = []
""" :type: list of strings, value: ["line1", "line2", "line3"] """




##################### init services #################################
_screen = Screen()
_wifi = Wifi()
# messager = Message(screen)
# messager.displayMessage('welcome')
# utime.sleep(1)
# button = Button()

########################### init devices ################################

buzzer = Buzzer()
# mqtt = Mqtt(messager, button, buzzer)
buzzer.bip(0.1)

_screen.showHome(WIFI_STATUS)


###################################################################
####################### MAIN LOOP #################################
###################################################################

while RUNNING:
     ####################### COLLECT STATUS AND UPDATE GLOBAL STATUS VAR ##############################




    ####################### EXECUTE ACTIONS BASED ON GLOBAL STATUS VAR ##############################

    ###### wifi  ####
    try:
         WIFI_STATUS = _wifi.auto_manage(WIFI_STATUS)
    except Exception as e:
        print("wifi execption in main loop")
        print(e)
        WIFI_STATUS = "disconnected"

    ###### update screen #########
    try:
        _screen.showHome(WIFI_STATUS)
    except Exception as e:
        print("screen show home execption in main loop")
        print(e)
    utime.sleep(2)


