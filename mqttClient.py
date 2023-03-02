import machine as machine
import json
import utime
from machine import Pin
from lib.umqtt.simple import MQTTClient
from conf.conf import MQTT_TOPIC_NAME, MQTT_BROKER_URL, DEVICE_UUID


class Mqtt:
    client = MQTTClient(client_id=DEVICE_UUID, server=MQTT_BROKER_URL, port=1883)

    def connectToBroker(self):
        try:
            self.client.connect()
            return "connected"
        except Exception as e:
            print("connect to broker error", e)
            return "disconnected"

    def subscribeToTopic(self, topic_name):
        try:
            self.client.subscribe(topic_name)
            return "topicName"
        except Exception as e:
            print("subscribe to topic error", e)
            return "none"

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
