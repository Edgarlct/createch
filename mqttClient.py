import machine as machine
import json
import utime
from machine import Pin
from lib.umqtt.simple import MQTTClient
from conf.conf import MQTT_TOPIC_NAME, MQTT_BROKER_URL, DEVICE_UUID


class Mqtt:
    status = 'disconected'  # disconnected, connecting, connected
    connectedToBroker = False
    client = False

    def __init__(self, messager, mainButton, buzzer):
        self.client = MQTTClient(client_id='bouldog', server=MQTT_BROKER_URL, port=1883)
        self.led = machine.Pin("LED", machine.Pin.OUT)
        self.mqttInit()
        self.messager = messager
        self.button = mainButton
        self.buzzer = buzzer
        print('mqtt constructor end')

    def mqttInit(self):
        self.status = 'connecting'
        self.connectedToBroker = self.connectToBroker()
        if self.connectedToBroker:
            print('mqtt full connected to broker')

    def connectToBroker(self):
        while not self.connectedToBroker:
            try:
                self.client.set_callback(self.sub_cb)
                self.client.connect()
                print('connected to broker')
                self.connectedToBroker = True
                return True
            except Exception as e:
                print('connect to broker error')
                self.connectedToBroker = False
                print(e)
                return False
        utime.sleep(1)
        self.status = 'connected'

    def subscribeToTopic(self, topicName):
        try:
            self.client.subscribe(topicName)
            return True
        except Exception as e:
            print(e)
            return False

    def sub_cb(self, topic, msg):
        msg = msg.decode('utf8').replace("'", '"')
        msg = json.loads(msg)

        if DEVICE_UUID in msg["targets"]:
            msg['readed'] = False
            while not msg['readed']:
                if self.button.isPressed():
                    msg['readed'] = True
                    self.buzzer.bip(0.2)
                    break
                else:
                    self.messager.showUnreadMessage(self.button)
                    self.buzzer.bip(0.2)
            self.messager.displayinDefinitelyMessage(msg['message'])
