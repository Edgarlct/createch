import _thread

from Button import Button
from Buzzer import Buzzer
from Screen import Screen
from Wifi import Wifi
import utime
from Message import Message
from conf.conf import MQTT_TOPIC_NAME, DEVICE_UUID
from mqttClient import Mqtt

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
MQTT_CONNECTION_TO_BROKER_STATUS = "disconnected"
""":type: str, value: "connected" or "disconnected" """

MQTT_SUBSCRIBED_TOPIC = "none"
""" :type: str, value: "none" or <topic name> """

########## BUTTONS ##########
MAIN_BUTTON_SHORT_PRESSED = False
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
HOME_TEXTS = [DEVICE_UUID, MQTT_SUBSCRIBED_TOPIC, "no error"]
""" :type: list of strings, value: ["line1", "line2", "line3"] """


##################### init services #################################
_screen = Screen()
_wifi = Wifi()
_messager = Message(_screen)
_button = Button()
_mqtt = Mqtt()

########################### init devices ################################

buzzer = Buzzer()

# _screen.showHome(WIFI_STATUS, mqtt_status=MQTT_CONNECTION_TO_BROKER_STATUS, home_texts=HOME_TEXTS)

###################################################################
####################### MAIN LOOP #################################
###################################################################

def ui_loop():
    global MAIN_BUTTON_SHORT_PRESSED
    while True:
        if _button.MainIsPressed():
            MAIN_BUTTON_SHORT_PRESSED = True

        #update screen
        try:
            _screen.showHome(wifiStatus=WIFI_STATUS, mqtt_status=MQTT_CONNECTION_TO_BROKER_STATUS,
                             home_texts=HOME_TEXTS)
        except Exception as e:
            print("screen show home execption in main loop")
            print(e)
        utime.sleep(0.1)

THREAD1 = _thread.start_new_thread(ui_loop, ())


while RUNNING:
    ####################### EXECUTE ACTIONS BASED ON GLOBAL STATUS VAR ##############################

    ###### wifi  ####
    try:
         WIFI_STATUS = _wifi.auto_manage(WIFI_STATUS)
    except Exception as e:
        print("wifi execption in main loop")
        print(e)
        WIFI_STATUS = "disconnected"


    ###### mqtt ####
    if WIFI_STATUS == "connected" and MQTT_CONNECTION_TO_BROKER_STATUS == "disconnected":
        MQTT_CONNECTION_TO_BROKER_STATUS = _mqtt.connect_to_broker()

    if MQTT_CONNECTION_TO_BROKER_STATUS == "connected" and MQTT_SUBSCRIBED_TOPIC == "none":
        MQTT_SUBSCRIBED_TOPIC = _mqtt.subscribe_to_topic(MQTT_TOPIC_NAME, RECEIVED_MESSAGE_CUE)

    try:
        if MQTT_SUBSCRIBED_TOPIC != "none":
            _mqtt.client.check_msg()
            if len(RECEIVED_MESSAGE_CUE) > 0:
                print(RECEIVED_MESSAGE_CUE[0]["message"])
                while not RECEIVED_MESSAGE_CUE[0]["readed"]:
                    buzzer.bip(1)
                    if MAIN_BUTTON_SHORT_PRESSED:
                        RECEIVED_MESSAGE_CUE[0]["readed"] = True
                        RECEIVED_MESSAGE_CUE.pop(0)
                        MAIN_BUTTON_SHORT_PRESSED = False

    except Exception as e:
        print("check msg execption in main loop")
        print(e)

    ###### update texts ######
    HOME_TEXTS = [DEVICE_UUID, MQTT_SUBSCRIBED_TOPIC, "no error"]

    utime.sleep(0.2)




