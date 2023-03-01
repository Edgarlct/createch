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

    def __init__(self, messager):
        self.client = MQTTClient(client_id='bouldog', server=MQTT_BROKER_URL, port=1883)
        self.led = machine.Pin("LED", machine.Pin.OUT)
        self.mqttInit()
        self.messager = messager

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
            self.messager.displayinDefinitelyMessage(msg["message"])
            print(msg["message"])
            self.led.on()
            utime.sleep(0.5)
            self.led.off()
            utime.sleep(0.5)
            self.led.on()
            utime.sleep(0.5)
            self.led.off()
